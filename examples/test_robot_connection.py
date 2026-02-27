
from lerobot_robot_so_sensor_arm import SOSensorArmConfig
from lerobot_robot_so_sensor_arm import SOSensorArm

so_follower_port = "/dev/YOUR_ROBOT_SERIAL_PORT" # example: "/dev/ttyACM0"
force_sensor_port = "/dev/YOUR_SENSOR_SERIAL_PORT" # example: "/dev/ttyACM2"

config = SOSensorArmConfig(port=so_follower_port, sensor_port=force_sensor_port)
arm = SOSensorArm(config)

arm.connect(calibrate=False)
obs = arm.get_observation()
print(obs)
