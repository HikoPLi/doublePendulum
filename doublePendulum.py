import math
import pygame

# 初始化程序
pygame.init()

# 设置窗口大小
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Double Pendulum Simulation")

# 设置模拟参数
length1 = 200  # 第一根摆杆长度
length2 = 150  # 第二根摆杆长度
mass1 = 20  # 第一根摆杆质量
mass2 = 10  # 第二根摆杆质量
gravity = 9.81  # 重力加速度
theta1 = math.pi / 2  # 第一根摆杆初始角度
theta2 = math.pi / 2  # 第二根摆杆初始角度
theta1_velocity = 0  # 第一根摆杆角速度
theta2_velocity = 0  # 第二根摆杆角速度
time_step = 0.05  # 时间步长

# 循环计算摆的位置
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 计算摆的位置
    alpha = mass1 + mass2
    beta = mass2 * length1 * math.cos(theta1 - theta2)
    gamma = length1 * (alpha * length1 - mass2 *
                       length2 * math.cos(theta1 - theta2))
    delta = mass2 * length2 * math.cos(theta1 - theta2)
    epsilon = mass1 * length1 + mass2 * length2

    theta1_acceleration = (gravity * (mass2 * math.sin(theta2) * math.cos(theta1 - theta2) - alpha * math.sin(theta1)) - (
        delta * theta2_velocity ** 2 + epsilon * theta1_velocity ** 2 * math.sin(theta1 - theta2)) * math.sin(theta1 - theta2)) / gamma
    theta2_acceleration = (gravity * (alpha * math.sin(theta1) * math.cos(theta1 - theta2) - mass2 * math.sin(theta2)) + (
        epsilon * theta2_velocity ** 2 + delta * theta1_velocity ** 2 * math.sin(theta1 - theta2)) * math.sin(theta1 - theta2)) / gamma

    theta1_velocity += theta1_acceleration * time_step
    theta2_velocity += theta2_acceleration * time_step

    theta1 += theta1_velocity * time_step
    theta2 += theta2_velocity * time_step

    # 绘制摆的位置
    x1 = length1 * math.sin(theta1) + window_size[0] / 2
    y1 = length1 * math.cos(theta1) + window_size[1] / 2

    x2 = x1 + length2 * math.sin(theta2)
    y2 = y1 + length2 * math.cos(theta2)

    pygame.draw.line(screen, (255, 255, 255),
                     (window_size[0] / 2, window_size[1] / 2), (x1, y1), 5)
    pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 5)

    # 更新屏幕
    pygame.display.flip()
