from machine import Pin, ADC, PWM
import utime

pot = machine.ADC(26) 
led = PWM(Pin(25))
led.freq(25000)
fan = PWM(Pin(21))
fan.freq(25000)
sensor_temp = machine.ADC(4)
conversion_factor = 3.26 / (65535)


def map (x, in_min, in_max, out_min, out_max):
  """ Maps two ranges together """
  return int ((x-in_min) * (out_max-out_min) / (in_max - in_min) + out_min)

 
while True:
  t1 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t2 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t3 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t4 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t5 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t6 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t7 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t8 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t9 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t10 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t11 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t12 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t13 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t14 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t15 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t16 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t17 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t18 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t19 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t20 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t21 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t22 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t23 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t24 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t25 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t26 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t27 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t28 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t29 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  t30 = sensor_temp.read_u16() * conversion_factor
  utime.sleep(0.01)
  
  raw_temps = (t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t10,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25,t26,t27,t28,t29,t30)
  avg_temp = sum(raw_temps)/30
  temperature = 27 - (avg_temp - 0.706)/0.001721
  temp_f = round((temperature * 1.8 + 32),1)
  temp_percent = map(temperature,15,45,0,100)


  pot_value = pot.read_u16()
  pot_percentage = map(pot_value,300,65535,100,100)

  output_percentage = (temp_percent * pot_percentage / 100)
  

  pwm_value = map(output_percentage,0,100,0,65535)

  pwm_output = min(max(9830,pwm_value),65535)
  
  
  print("Temp C:",temperature, "Temp F:",temp_f, "Temp percentage:",temp_percent, "Pot Percentage:",pot_percentage, "Pot Value",pot_value, "Final Percent",output_percentage,"pwm value",pwm_value,"Output PWM",pwm_output)
  led.duty_u16(pwm_output)
  fan.duty_u16(pwm_output)
  utime.sleep(0.01)
