# WORAD

**Current progress with app.py**: This code when running app.py opens a local web server which address will be displayed in the terminal. Reading from the serial COM port connected to the Arduino board, the python script splits the data by looking for pairs (name of the sensor and value attributed during the loop) separated by semi-colons [;]. The value for each sensor is then passed to the web server and displayed on the corresponding graph.

⚠test.py is only for checking serial communication with arduino board and data splitting.

**Main known issues**: 
  - Initialisation must be done with the arduino IDE Serial monitor open, for establishing communication // _pottential fix_: remove the serial.print from arduino code for initialisation
  - BME680 sensor still erroring out // _potential solution_: arduino library modification
  - Serial connection sometimes unstable// _potential solution_: curently handling exceptions with reconnection and timeouts, working on establishing bluetooth connection and avoid using serial communication
## 


## Arduino specifications
### Sensors

### Main control board

