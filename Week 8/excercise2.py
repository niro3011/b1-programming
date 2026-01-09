from datetime import datetime, timedelta
from typing import List, Dict, Optional
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class UserRole(Enum):
    """Enum for user roles"""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class DeviceType(Enum):
    """Enum for device types"""
    LAPTOP = "laptop"
    DESKTOP = "desktop"
    MOBILE = "mobile"
    TABLET = "tablet"
    IOT = "iot"
    SERVER = "server"


class Device:

    def __init__(self, device_id: str, device_type: DeviceType, 
                 firmware_version: str, owner: str):
        self.device_id = device_id
        self.device_type = device_type
        self.firmware_version = firmware_version
        self.compliance_status = False
        self.owner = owner
        self.last_security_scan: Optional[datetime] = None
        self.is_active = True
        self.is_quarantined = False
        self.authorized_users: List[str] = [owner]
        self.admin_users: List[str] = []
        
        logger.info(f"Device {device_id} created - Type: {device_type.value}, Owner: {owner}")
    
    def authorize_access(self, user: str, role: UserRole = UserRole.USER) -> bool:

        if self.is_quarantined:
            logger.warning(f"Access denied to {user} - Device {self.device_id} is quarantined")
            return False
        
        if not self.is_active:
            logger.warning(f"Access denied to {user} - Device {self.device_id} is inactive")
            return False

        if role == UserRole.ADMIN or user in self.admin_users:
            logger.info(f"Admin access granted to {user} for device {self.device_id}")
            return True

        if user in self.authorized_users:
            logger.info(f"Access granted to {user} for device {self.device_id}")
            return True
        
        logger.warning(f"Access denied to {user} for device {self.device_id}")
        return False
    
    def update_firmware(self, new_version: str, user: str, role: UserRole = UserRole.USER) -> bool:

        if not self.authorize_access(user, role):
            logger.error(f"Firmware update failed - User {user} not authorized for device {self.device_id}")
            return False
        
        old_version = self.firmware_version
        self.firmware_version = new_version
        logger.info(f"Device {self.device_id} firmware updated from {old_version} to {new_version} by {user}")
        
        # Firmware update triggers security scan requirement
        self.compliance_status = False
        return True
    
    def run_security_scan(self, user: str, role: UserRole = UserRole.USER) -> Dict[str, any]:

        if not self.authorize_access(user, role):
            logger.error(f"Security scan failed - User {user} not authorized for device {self.device_id}")
            return {"success": False, "message": "Access denied"}
        
        self.last_security_scan = datetime.now()
        scan_result = {
            "success": True,
            "device_id": self.device_id,
            "scan_time": self.last_security_scan,
            "firmware_version": self.firmware_version,
            "vulnerabilities_found": 0,  # Simulated
            "message": "Security scan completed successfully"
        }
        
        logger.info(f"Security scan completed on device {self.device_id} by {user}")
        
        # Update compliance after scan
        self.check_compliance()
        
        return scan_result
    
    def check_compliance(self, override_user: Optional[str] = None, 
                        override_role: UserRole = UserRole.USER) -> bool:

        if override_user and override_role == UserRole.ADMIN:
            self.compliance_status = True
            logger.warning(f"Compliance override applied by admin {override_user} for device {self.device_id}")
            return True
        
        if self.last_security_scan is None:
            self.compliance_status = False
            logger.info(f"Device {self.device_id} non-compliant - No security scan performed")
            return False
        
        days_since_scan = (datetime.now() - self.last_security_scan).days
        
        if days_since_scan > 30:
            self.compliance_status = False
            logger.warning(f"Device {self.device_id} non-compliant - Last scan {days_since_scan} days ago")
            return False
        
        self.compliance_status = True
        logger.info(f"Device {self.device_id} is compliant - Last scan {days_since_scan} days ago")
        return True
    
    def quarantine(self, user: str, role: UserRole, reason: str = "Security concern") -> bool:

        if role != UserRole.ADMIN:
            logger.error(f"Quarantine failed - User {user} does not have admin privileges")
            return False
        
        self.is_quarantined = True
        self.is_active = False
        logger.critical(f"Device {self.device_id} QUARANTINED by {user} - Reason: {reason}")
        return True
    
    def release_quarantine(self, user: str, role: UserRole) -> bool:

        if role != UserRole.ADMIN:
            logger.error(f"Quarantine release failed - User {user} does not have admin privileges")
            return False
        
        self.is_quarantined = False
        self.is_active = True
        logger.info(f"Device {self.device_id} released from quarantine by {user}")
        return True
    
    def add_authorized_user(self, user: str, admin: str, admin_role: UserRole) -> bool:
        if admin_role != UserRole.ADMIN and admin not in self.admin_users:
            logger.error(f"Failed to add user - {admin} does not have admin privileges")
            return False
        
        if user not in self.authorized_users:
            self.authorized_users.append(user)
            logger.info(f"User {user} added to authorized users for device {self.device_id}")
            return True
        return False
    
    def __repr__(self) -> str:
        return (f"Device(id={self.device_id}, type={self.device_type.value}, "
                f"firmware={self.firmware_version}, compliant={self.compliance_status}, "
                f"active={self.is_active}, quarantined={self.is_quarantined})")


class DeviceManager:

    def __init__(self):
        self.devices: Dict[str, Device] = {}
        logger.info("DeviceManager initialized")
    
    def add_device(self, device: Device) -> bool:

        if device.device_id in self.devices:
            logger.warning(f"Device {device.device_id} already exists in manager")
            return False
        
        self.devices[device.device_id] = device
        logger.info(f"Device {device.device_id} added to manager")
        return True
    
    def remove_device(self, device_id: str, user: str, role: UserRole) -> bool:

        if role != UserRole.ADMIN:
            logger.error(f"Device removal failed - User {user} does not have admin privileges")
            return False
        
        if device_id not in self.devices:
            logger.warning(f"Device {device_id} not found in manager")
            return False
        
        del self.devices[device_id]
        logger.info(f"Device {device_id} removed from manager by {user}")
        return True
    
    def get_device(self, device_id: str) -> Optional[Device]:
        """Get a device by ID"""
        return self.devices.get(device_id)
    
    def generate_security_report(self) -> Dict[str, any]:
        """
        Generate comprehensive security report for all devices
        
        Returns:
            dict: Security report with statistics and device details
        """
        total_devices = len(self.devices)
        active_devices = sum(1 for d in self.devices.values() if d.is_active)
        compliant_devices = sum(1 for d in self.devices.values() if d.compliance_status)
        quarantined_devices = sum(1 for d in self.devices.values() if d.is_quarantined)
        never_scanned = sum(1 for d in self.devices.values() if d.last_security_scan is None)
        
        needs_scan = []
        for device in self.devices.values():
            if device.last_security_scan is None:
                needs_scan.append({
                    "device_id": device.device_id,
                    "reason": "Never scanned"
                })
            elif (datetime.now() - device.last_security_scan).days > 30:
                days_overdue = (datetime.now() - device.last_security_scan).days - 30
                needs_scan.append({
                    "device_id": device.device_id,
                    "reason": f"Scan overdue by {days_overdue} days"
                })
        
        report = {
            "report_generated": datetime.now(),
            "summary": {
                "total_devices": total_devices,
                "active_devices": active_devices,
                "compliant_devices": compliant_devices,
                "non_compliant_devices": total_devices - compliant_devices,
                "quarantined_devices": quarantined_devices,
                "never_scanned": never_scanned,
                "compliance_rate": f"{(compliant_devices/total_devices*100):.2f}%" if total_devices > 0 else "0%"
            },
            "devices_needing_attention": needs_scan,
            "quarantined_devices": [
                device.device_id for device in self.devices.values() if device.is_quarantined
            ]
        }
        
        logger.info("Security report generated")
        return report
    
    def get_non_compliant_devices(self) -> List[Device]:
        """Get list of non-compliant devices"""
        return [device for device in self.devices.values() if not device.compliance_status]
    
    def bulk_compliance_check(self) -> int:
        """
        Run compliance check on all devices
        
        Returns:
            int: Number of non-compliant devices found
        """
        non_compliant_count = 0
        for device in self.devices.values():
            if not device.check_compliance():
                non_compliant_count += 1
        
        logger.info(f"Bulk compliance check completed - {non_compliant_count} non-compliant devices found")
        return non_compliant_count


if __name__ == "__main__":
    manager = DeviceManager()
    
    device1 = Device("DEV001", DeviceType.LAPTOP, "v2.1.0", "john_doe")
    device2 = Device("DEV002", DeviceType.MOBILE, "v1.5.3", "jane_smith")
    device3 = Device("DEV003", DeviceType.SERVER, "v3.0.1", "admin_user")
    
    manager.add_device(device1)
    manager.add_device(device2)
    manager.add_device(device3)
    
    device1.run_security_scan("john_doe", UserRole.USER)
    device2.run_security_scan("jane_smith", UserRole.USER)
    
    device1.update_firmware("v2.2.0", "john_doe", UserRole.USER)
    
    device1.check_compliance()
    device2.check_compliance()
    device3.check_compliance()
    
    device3.quarantine("admin_user", UserRole.ADMIN, "Malware detected")
    
    report = manager.generate_security_report()
    print("\n=== SECURITY REPORT ===")
    print(f"Total Devices: {report['summary']['total_devices']}")
    print(f"Compliant: {report['summary']['compliant_devices']}")
    print(f"Non-Compliant: {report['summary']['non_compliant_devices']}")
    print(f"Quarantined: {report['summary']['quarantined_devices']}")
    print(f"Compliance Rate: {report['summary']['compliance_rate']}")
    print(f"\nDevices Needing Attention: {len(report['devices_needing_attention'])}")
    for device in report['devices_needing_attention']:
        print(f"  - {device['device_id']}: {device['reason']}")