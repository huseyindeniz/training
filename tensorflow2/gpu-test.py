import tensorflow as tf
import time

print(('Is your GPU available for use?\n{0}').format(
    'Yes, your GPU is available: True' if tf.test.is_gpu_available() == True else 'No, your GPU is NOT available: False'
))

print(('\nYour devices that are available:\n{0}').format(
    [device.name for device in tf.config.experimental.list_physical_devices()]
))

cpu_slot = 0
gpu_slot = 0

# Using CPU at slot 0
with tf.device('/CPU:' + str(cpu_slot)):
    # Starting a timer
    start = time.time()

    # Doing operations on CPU
    A = tf.constant([[3, 2], [5, 2]])
    print(tf.eye(2,2))

    # Printing how long it took with CPU
    end = time.time() - start
    print(end)

# Using the GPU at slot 0
with tf.device('/GPU:' + str(gpu_slot)):
    # Starting a timer
    start = time.time()

    # Doing operations on CPU
    A = tf.constant([[3, 2], [5, 2]])
    print(tf.eye(2,2))

    # Printing how long it took with CPU
    end = time.time() - start
    print(end)
