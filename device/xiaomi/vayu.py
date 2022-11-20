from build_kernel.utils.device import register_device
from device.xiaomi.sm8150 import XiaomiSM8150Device

class XiaomiVayuDevice(XiaomiSM8150Device):
	PRODUCT_DEVICE = "vayu"
	TARGET_KERNEL_FRAGMENTS = ["vendor/vayu_defconfig"]

register_device(XiaomiVayuDevice)
