import graph as g
import math
import time

window_width = 640
window_height = 442
g.windowSize(window_width, window_height)
g.canvasSize(window_width, window_height)

picture_width = 600
frame_thickness = (window_width - picture_width) / 2
pen_width_0 = 0
pen_width_1 = 1

g.penSize(pen_width_0)

width_line_of_sky = 191
sky_upper_left_point_x = 20
sky_upper_left_point_y = 20
sky_bottom_right_point_x = sky_upper_left_point_x + picture_width
sky_bottom_right_point_y = sky_upper_left_point_y + width_line_of_sky
sky_color = '#94ffff'
g.brushColor(sky_color)
g.rectangle(sky_upper_left_point_x, sky_upper_left_point_y,
            sky_bottom_right_point_x, sky_bottom_right_point_y)

amplitude_sin_beach = 8
period_sin_beach = 88

width_line_of_sea = 101
sea_upper_left_point_x = sky_upper_left_point_x
sea_upper_left_point_y = sky_bottom_right_point_y
sea_bottom_right_point_x = sky_bottom_right_point_x
sea_bottom_right_point_y = sea_upper_left_point_y + width_line_of_sea
sea_color = '#4c00ff'
g.brushColor(sea_color)
g.rectangle(sea_upper_left_point_x, sea_upper_left_point_y,
            sea_bottom_right_point_x, sea_bottom_right_point_y + amplitude_sin_beach)

width_line_of_beach = 124
beach_upper_left_point_x = sea_upper_left_point_x
beach_upper_left_point_y = sea_bottom_right_point_y
beach_bottom_right_point_x = sea_bottom_right_point_x
beach_bottom_right_point_y = beach_upper_left_point_y + width_line_of_beach
beach_color = '#ede900'
g.brushColor(beach_color)
g.penColor(beach_color)

sea_line_points = [(beach_bottom_right_point_x, beach_upper_left_point_y + amplitude_sin_beach),
                   (beach_bottom_right_point_x, beach_bottom_right_point_y),
                   (beach_upper_left_point_x, beach_bottom_right_point_y)]

number_of_points = 500
x = beach_upper_left_point_x
step_x = picture_width / number_of_points

for i in range(number_of_points):
    y = beach_upper_left_point_y + amplitude_sin_beach * math.cos(2 * math.pi * x / period_sin_beach)
    sea_line_points.append((x, y))
    x += step_x

sea_line_points.append((beach_bottom_right_point_x, beach_upper_left_point_y + amplitude_sin_beach))
g.polygon(sea_line_points)

center_of_sun_x = 537
center_of_sun_y = 84
number_of_corners = 50
inner_radius_of_sun = 47
outer_radius_of_sun = 57
angle_of_corner = 0
step_of_angle = math.pi / number_of_corners

corners_of_sun = []
for i in range(2 * number_of_corners):
    if i % 2:
        x = center_of_sun_x + inner_radius_of_sun * math.cos(angle_of_corner)
        y = center_of_sun_y + inner_radius_of_sun * math.sin(angle_of_corner)
    else:
        x = center_of_sun_x + outer_radius_of_sun * math.cos(angle_of_corner)
        y = center_of_sun_y + outer_radius_of_sun * math.sin(angle_of_corner)

    corners_of_sun.append((x, y))
    angle_of_corner += step_of_angle

corners_of_sun.append((center_of_sun_x + outer_radius_of_sun, center_of_sun_y))
sun_color = 'yellow'
g.brushColor(sun_color)
g.penColor(sun_color)
g.polygon(corners_of_sun)


def draw_an_ellipse(ellipse_center_x, ellipse_center_y,
                    amplitude_x, amplitude_y):
    angle = 0
    details = 300
    angle_step = 2 * math.pi / details
    points = []
    for _ in range(details):
        x_coord = ellipse_center_x + amplitude_x * math.cos(angle)
        y_coord = ellipse_center_y + amplitude_y * math.sin(angle)
        points.append((x_coord, y_coord))
        angle += angle_step

    points.append((ellipse_center_x + amplitude_x, ellipse_center_y))
    obj = g.polygon(points)
    return obj


def draw_clouds(center_of_the_fisrt_cloud_x, center_of_the_first_cloud_y,
                cloud_radius_x, cloud_radius_y):
    cloud_object = []
    g.penSize(pen_width_1)
    cloud_color = 'white'
    g.brushColor(cloud_color)
    g.penColor('grey')
    step_of_clouds = 3 / 2 * cloud_radius_x

    center_cloud_1_x = center_of_the_fisrt_cloud_x
    center_cloud_1_y = center_of_the_first_cloud_y
    number_of_clouds_1 = 2
    for _ in range(number_of_clouds_1):
        obj = draw_an_ellipse(center_cloud_1_x, center_cloud_1_y, cloud_radius_x, cloud_radius_y)
        center_cloud_1_x += step_of_clouds
        cloud_object.append(obj)

    center_cloud_2_x = center_of_the_fisrt_cloud_x - cloud_radius_x
    center_cloud_2_y = center_of_the_first_cloud_y + cloud_radius_y
    number_of_clouds_2 = 3
    for _ in range(number_of_clouds_2):
        obj = draw_an_ellipse(center_cloud_2_x, center_cloud_2_y, cloud_radius_x, cloud_radius_y)
        center_cloud_2_x += step_of_clouds
        cloud_object.append(obj)

    obj1 = draw_an_ellipse(center_cloud_1_x, center_cloud_1_y, cloud_radius_x, cloud_radius_y)
    cloud_object.append(obj1)
    obj2 = draw_an_ellipse(center_cloud_2_x, center_cloud_2_y, cloud_radius_x, cloud_radius_y)
    cloud_object.append(obj2)

    return cloud_object


center_of_the_fisrt_cloud_1_x = 152
center_of_the_first_cloud_1_y = 73
cloud_1_radius_x = 14
cloud_1_radius_y = 14
cloud1 = draw_clouds(center_of_the_fisrt_cloud_1_x, center_of_the_first_cloud_1_y,
                     cloud_1_radius_x, cloud_1_radius_y)

center_of_the_fisrt_cloud_2_x = 295
center_of_the_first_cloud_2_y = 55
cloud_2_radius_x = 24
cloud_2_radius_y = 27
cloud2 = draw_clouds(center_of_the_fisrt_cloud_2_x, center_of_the_first_cloud_2_y,
                     cloud_2_radius_x, cloud_2_radius_y)

center_of_the_fisrt_cloud_3_x = 110
center_of_the_first_cloud_3_y = 135
cloud_3_radius_x = 22
cloud_3_radius_y = 15
cloud3 = draw_clouds(center_of_the_fisrt_cloud_3_x, center_of_the_first_cloud_3_y,
                     cloud_3_radius_x, cloud_3_radius_y)


def draw_an_umbrella(umbrella_base_x, umbrella_base_y,
                     umbrella_stick_length, umbrella_stick_width,
                     umbrella_triangle_base, umbrella_triangle_height):
    g.penSize(umbrella_stick_width)
    umbrella_color = '#c56200'
    g.penColor(umbrella_color)

    fi = math.pi / 180 * 20
    for _ in range(umbrella_stick_length // 2):
        dx_umbrella = math.sin(fi) * 2
        dy = math.cos(fi) * 2
        g.line(umbrella_base_x, umbrella_base_y,
               umbrella_base_x + dx_umbrella, umbrella_base_y - dy)  # umbrella_triangle_left_angle_y)
        umbrella_base_x += dx_umbrella
        umbrella_base_y -= dy
        fi += math.pi / 180 * 0.5

    umbrella_triangle_right_angle_x = umbrella_base_x + umbrella_triangle_base * math.cos(fi) / 2
    umbrella_triangle_left_angle_y = umbrella_base_y - umbrella_triangle_base * math.sin(fi) / 2

    umbrella_triangle_left_angle_x = umbrella_base_x - umbrella_triangle_base * math.cos(fi) / 2
    umbrella_triangle_right_angle_y = umbrella_base_y + umbrella_triangle_base * math.sin(fi) / 2

    umbrella_top_angle_x = umbrella_base_x + umbrella_triangle_height * math.sin(fi)
    umbrella_top_angle_y = umbrella_base_y - umbrella_triangle_height * math.cos(fi)

    g.penSize(pen_width_1)
    g.penColor('black')

    g.brushColor('#f66347')
    g.polygon([(umbrella_triangle_left_angle_x, umbrella_triangle_left_angle_y),
               (umbrella_triangle_right_angle_x, umbrella_triangle_right_angle_y),
               (umbrella_top_angle_x, umbrella_top_angle_y)])

    number_of_needle = 6
    needle_base_point_x = umbrella_triangle_left_angle_x
    needle_base_point_y = umbrella_triangle_left_angle_y
    step_needle_x = umbrella_triangle_base / 7 * math.cos(fi)
    step_needle_y = umbrella_triangle_base / 7 * math.sin(fi)
    for _ in range(number_of_needle):
        needle_base_point_x += step_needle_x
        needle_base_point_y += step_needle_y

        g.line(umbrella_top_angle_x, umbrella_top_angle_y,
               needle_base_point_x, needle_base_point_y)


umbrella_1_base_x = 112
umbrella_1_base_y = 410
umbrella_1_stick_length = 120
umbrella_1_stick_width = 6
umbrella_1_triangle_base = 138
umbrella_1_triangle_height = 43

draw_an_umbrella(umbrella_1_base_x, umbrella_1_base_y,
                 umbrella_1_stick_length, umbrella_1_stick_width,
                 umbrella_1_triangle_base, umbrella_1_triangle_height)

umbrella_2_base_x = 228
umbrella_2_base_y = 390
umbrella_2_stick_length = 80
umbrella_2_stick_width = 3
umbrella_2_triangle_base = 58
umbrella_2_triangle_height = 24

draw_an_umbrella(umbrella_2_base_x, umbrella_2_base_y,
                 umbrella_2_stick_length, umbrella_2_stick_width,
                 umbrella_2_triangle_base, umbrella_2_triangle_height)


def points_of_stern(center_of_stern_x, center_of_stern_y, radius_of_stern):
    angle = 0
    number_of_points_of_stern = 100
    stern_step_of_angle = math.pi / 2 / number_of_points_of_stern
    points = []

    for _ in range(number_of_points_of_stern):
        angle += stern_step_of_angle
        x_of_stern = center_of_stern_x - radius_of_stern * math.cos(angle)
        y_of_stern = center_of_stern_y + radius_of_stern * math.sin(angle)
        points.append((x_of_stern, y_of_stern))

    return points


def draw_a_ship(ship_bow_x, ship_size):
    ship_bow_y = sea_upper_left_point_y + ship_size * (225 - sea_upper_left_point_y)

    ship_keel_x = ship_bow_x - ship_size * 65
    ship_keel_y = ship_bow_y + ship_size * 28

    ship_stern_top_x = ship_bow_x - ship_size * 209
    ship_stern_top_y = ship_bow_y

    ship_stern_bottom_x = ship_stern_top_x
    ship_stern_bottom_y = ship_keel_y

    ship_color = '#df6f0d'
    g.penColor(ship_color)
    g.brushColor(ship_color)
    ship_stern_radius = ship_stern_bottom_y - ship_stern_top_y

    points_of_ship = [(ship_stern_bottom_x, ship_stern_bottom_y),
                      (ship_keel_x, ship_keel_y),
                      (ship_bow_x, ship_bow_y),
                      (ship_stern_top_x - ship_stern_radius, ship_stern_top_y)]

    points_of_ship += points_of_stern(ship_stern_top_x, ship_stern_top_y, ship_stern_radius)
    object_1 = g.polygon(points_of_ship)

    g.penColor(sea_color)
    g.penSize(pen_width_1)
    object_2 = g.line(ship_stern_top_x, ship_stern_top_y, ship_stern_bottom_x, ship_stern_bottom_y)
    object_3 = g.line(ship_keel_x, ship_bow_y, ship_keel_x, ship_keel_y)

    ship_porthole_center_x = ship_bow_x - ship_size * 50
    ship_porthole_center_y = ship_bow_y + ship_size * 11
    ship_porthole_radius = ship_size * 7
    porthole_pen_width = ship_size * 3.25
    g.penSize(porthole_pen_width)
    g.penColor('black')
    portole_color = 'white'
    g.brushColor(portole_color)
    object_4 = g.circle(ship_porthole_center_x, ship_porthole_center_y, ship_porthole_radius)

    mast_base_x = ship_bow_x - ship_size * 150
    mast_base_y = ship_bow_y
    mast_hight = ship_size * 96
    mast_width = ship_size * 6

    g.penSize(mast_width)
    mast_color = 'black'
    g.penColor(mast_color)
    object_5 = g.line(mast_base_x, mast_base_y, mast_base_x, mast_base_y - mast_hight)

    sail_top_mount_x = mast_base_x
    sail_top_mount_y = mast_base_y - mast_hight
    sail_bottom_mount_x = mast_base_x
    sail_bottom_mount_y = mast_base_y
    sail_left_edge_x = ship_bow_x - ship_size * 134
    sail_left_edge_y = (sail_top_mount_y + sail_bottom_mount_y) / 2
    sail_right_edge_x = ship_bow_x - ship_size * 96
    sail_right_edge_y = sail_left_edge_y

    g.penSize(pen_width_1)
    g.penColor('black')
    sail_color = '#c9c094'
    g.brushColor(sail_color)
    object_6 = g.polygon([(sail_top_mount_x, sail_top_mount_y),
                          (sail_left_edge_x, sail_left_edge_y),
                          (sail_right_edge_x, sail_right_edge_y)])
    object_7 = g.polygon([(sail_bottom_mount_x, sail_bottom_mount_y),
                          (sail_left_edge_x, sail_left_edge_y),
                          (sail_right_edge_x, sail_right_edge_y)])

    return [object_1, object_2, object_3, object_4, object_5, object_6, object_7]


ship_1_bow_x = 296
ship_1_size = 0.43
objects_of_ship_1 = draw_a_ship(ship_1_bow_x, ship_1_size)

ship_2_bow_x = 0
ship_2_size = 1
objects_of_ship_2 = draw_a_ship(ship_2_bow_x, ship_2_size)

stern_of_ship = objects_of_ship_2[0]
ship_length = 237


def keyPressed():
    pause = 0.1
    time.sleep(pause)
    g.close()


def update():
    for object_ in objects_of_ship_2:
        g.moveObjectBy(object_, dx, 0)

    for object_ in cloud1:
        g.moveObjectBy(object_, dx / 3, 0)
    for object_ in cloud2:
        g.moveObjectBy(object_, dx * 2, 0)
    for object_ in cloud3:
        g.moveObjectBy(object_, dx * 1.5, 0)

    g.penColor('white')
    g.brushColor('white')
    g.rectangle(0, 0, frame_thickness, window_height)
    g.rectangle(window_width - frame_thickness, 0, window_width, window_height)

    if g.xCoord(stern_of_ship) > window_width:
        for object_ in objects_of_ship_2:
            g.moveObjectBy(object_, - window_width - ship_length, 0)

    if g.xCoord(cloud2[0]) > window_width:
        for object_ in cloud2:
            g.moveObjectBy(object_, - window_width - ship_length, 0)

    if g.xCoord(cloud1[0]) > window_width:
        for object_ in cloud1:
            g.moveObjectBy(object_, - window_width - ship_length, 0)

    if g.xCoord(cloud3[0]) > window_width:
        for object_ in cloud3:
            g.moveObjectBy(object_, - window_width - ship_length, 0)


dx = 3
update_time_ms = 50
g.onKey(keyPressed)
g.onTimer(update, update_time_ms)

g.run()
