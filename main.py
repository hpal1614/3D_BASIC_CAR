import maya.cmds as cmds

def create_car(name, length=2, width=1):
    # create car component
    body = create_body(length, width)
    tires = create_tires(length, width)

    final_name = assemble_car(name, body, tires)

    cmds.select(clear=True)

    return final_name


def create_body(length, width):
    body = cmds.polyPlane(w=length, h=width, name="body")
    return body[0]


def create_tires(body_length, body_width):
    tire_width = 0.25 * body_width
    tire_radius = 0.25 * body_length
    x_pos = 0.5 * body_length
    z_pos = 0.5 * body_width + 0.5 * tire_width

    fl_tire = create_tire("fornt_left_tier", tire_width, tire_width, x_pos, 0, -z_pos)
    fr_tire = create_tire("fornt_right_tier", tire_width, tire_width, x_pos, 0, z_pos)
    rl_tire = create_tire("rear_left_tier", tire_width, tire_width, -x_pos, 0, -z_pos)
    rr_tire = create_tire("rear_right_tier", tire_width, tire_width, -x_pos, 0, z_pos)

    return [fl_tire, fr_tire, rl_tire, rr_tire]


def create_tire(name, width, radius, tx, ty, tz):
    tire = cmds.polyCylinder(h=width, r=radius, ax=(0, 0, 1), sc=True, name=name)
    cmds.setAttr("{0}.translate".format(tire[0]), tx, ty, tz)
    return tire[0]


def assemble_car(name, body, tires):
    body_grp = cmds.group(body, name="body_grp")
    tires_grp = cmds.group(tires, name="tiers_grp")

    car_grp = cmds.group(body_grp, tires_grp, name="body")
    return car_grp


if __name__ == "__main__":
    final_name = create_car("test")
    print_car("Car created: {0}".format(final_name))
