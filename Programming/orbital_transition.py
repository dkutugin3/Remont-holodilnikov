import time
import krpc

conn = krpc.connect(name='Vessel speed')
vessel = conn.space_center.active_vessel
obt_frame = vessel.orbit.body.non_rotating_reference_frame
srf_frame = vessel.orbit.body.reference_frame

start_time = conn.space_center.ut
prev_time = start_time
with open("data/obt_tr.txt", mode="w", encoding="utf-8") as file:
    while True:
        cur_time = conn.space_center.ut
        if cur_time - prev_time >= 3600:
            obt_speed = vessel.flight(obt_frame).speed
            file.write(f"{(cur_time - start_time)/3600:.2f} {obt_speed:.2f}\n")
            prev_time = cur_time
