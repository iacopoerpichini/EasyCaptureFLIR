FLIR Blackfly S BFS-U3-123S6C
=============================

*Version: 1707.1.4.0*

Attributes
----------

`AasRoiEnable` : `bool`  
  Controls whether a user-specified ROI is used for auto algorithm that is currently selected by the AutoAlgorithmSelector feature.
  - default access: read/write
  - default value: `False`

`AasRoiEnableAddr` : `int`  
  
  - default access: read only
  - default value: `798720`
  - default range: -9223372036854775808 - 9223372036854775807

`AasRoiHeight` : `int`  
  Controls the width of the ROI used by the auto algorithm that is currently selected by the AutoAlgorithmSelector feature.
  - default access: not available
  - default range: 0 - 65535

`AasRoiHeightAddr` : `int`  
  
  - default access: read only
  - default value: `802816`
  - default range: -9223372036854775808 - 9223372036854775807

`AasRoiOffsetX` : `int`  
  Controls the x-offset of the ROI used by the auto algorithm that is currently selected by the AutoAlgorithmSelector feature.
  - default access: not available
  - default range: 0 - 65535

`AasRoiOffsetXAddr` : `int`  
  
  - default access: read only
  - default value: `799744`
  - default range: -9223372036854775808 - 9223372036854775807

`AasRoiOffsetY` : `int`  
  Controls the y-offset of the ROI used by the auto algorithm that is currently selected by the AutoAlgorithmSelector feature.
  - default access: not available
  - default range: 0 - 65535

`AasRoiOffsetYAddr` : `int`  
  
  - default access: read only
  - default value: `800768`
  - default range: -9223372036854775808 - 9223372036854775807

`AasRoiWidth` : `int`  
  Controls the width of the ROI used by the auto algorithm that is currently selected by the AutoAlgorithmSelector feature.
  - default access: not available
  - default range: 0 - 65535

`AasRoiWidthAddr` : `int`  
  
  - default access: read only
  - default value: `801792`
  - default range: -9223372036854775808 - 9223372036854775807

`AcquisitionBurstFrameCount` : `int`  
  This feature is used only if the FrameBurstStart trigger is enabled and the FrameBurstEnd trigger is disabled. Note that the total number of frames captured is also conditioned by AcquisitionFrameCount if AcquisitionMode is MultiFrame and ignored if AcquisitionMode is Single.
  - default access: read/write
  - default value: `1`
  - default range: 1 - 1000

`AcquisitionFrameCount` : `int`  
  Number of images to acquire during a multi frame acquisition.
  - default access: read/write
  - default value: `2`
  - default range: 2 - 65535

`AcquisitionFrameRate` : `float`  
  User controlled acquisition frame rate in Hertz
  - default access: read only
  - default value: `30.775457828020834`
  - unit: Hz
  - default range: 1.0 - 30.924259314510604

`AcquisitionFrameRateEnable` : `bool`  
  If enabled, AcquisitionFrameRate can be used to manually control the frame rate.
  - default access: read/write
  - default value: `False`

`AcquisitionLineRate` : `float`  
  Controls the rate (in Hertz) at which the Lines in a Frame are captured.
  - default access: read only
  - default value: `97465.88684210526`
  - unit: Hz
  - default range: 565.2783424908425 - 97465.88684210526

`AcquisitionMode` : `enum`  
  Sets the acquisition mode of the device. Continuous: acquires images continuously. Multi Frame: acquires a specified number of images before stopping acquisition. Single Frame: acquires 1 image before stopping acquisition.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values: `'Continuous'`, `'SingleFrame'`, `'MultiFrame'`

`AcquisitionResultingFrameRate` : `float`  
  Resulting frame rate in Hertz. If this does not equal the Acquisition Frame Rate it is because the Exposure Time is greater than the frame time.
  - default access: read only
  - default value: `30.775461585761057`
  - unit: Hz
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`AdcBitDepth` : `enum`  
  Selects which ADC bit depth to use. A higher ADC bit depth results in better image quality but slower maximum frame rate.
  - default access: read/write
  - default value: `'Bit10'`
  - possible values: `'Bit8'`, `'Bit10'`, `'Bit12'`, `'Bit14'`

`AutoAlgorithmSelector` : `enum`  
  Selects which Auto Algorithm is controlled by the RoiEnable, OffsetX, OffsetY, Width, Height features.
  - default access: read/write
  - default value: `'Awb'`
  - possible values:
    - `'Awb'`: Selects the Auto White Balance algorithm.
    - `'Ae'`: Selects the Auto Exposure algorithm.

`AutoAlgorithmSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`AutoExposureControlLoopDamping` : `float`  
  It controls how fast the exposure and gain get settled. If the value is too small, it may cause the system to be unstable. Range is from 0.0 to 1.0. Default = 0.2.
  - default access: read/write
  - default value: `0.5`
  - default range: 0.0 - 0.984375

`AutoExposureControlPriority` : `enum`  
  Selects whether to adjust gain or exposure first. When gain priority is selected, the camera fixes the gain to 0 dB, and the exposure is adjusted according to the target grey level. If the maximum exposure is reached before the target grey level is hit, the gain starts to change to meet the target. This mode is used to have the minimum noise. When exposure priority is selected, the camera sets the exposure to a small value (default is 5 ms). The gain is adjusted according to the target grey level. If maximum gain is reached before the target grey level is hit, the exposure starts to change to meet the target. This mode is used to capture fast motion.
  - default access: read/write
  - default value: `'Gain'`
  - possible values: `'Gain'`, `'ExposureTime'`

`AutoExposureEVCompensation` : `float`  
  The EV compensation value used in the exposure compensation. This allows you to adjust the resultant image intensity with one control. A positive value makes the image brighter. A negative value makes the image darker. Range from -3 to 3 with a step of 1/3. Default = 0.
  - default access: read/write
  - default value: `0.0`
  - default range: -3.0 - 3.0

`AutoExposureExposureTimeLowerLimit` : `float`  
  The smallest exposure time that auto exposure can set.
  - default access: read/write
  - default value: `100.0`
  - unit: us
  - default range: 10.0 - 15000.0

`AutoExposureExposureTimeUpperLimit` : `float`  
  The largest exposure time that auto exposure can set.
  - default access: read/write
  - default value: `15000.0`
  - unit: us
  - default range: 100.0 - 30000004.0

`AutoExposureGainLowerLimit` : `float`  
  The smallest gain that auto exposure can set.
  - default access: read/write
  - default value: `0.0`
  - unit: dB
  - default range: 0.0 - 18.000065071923338

`AutoExposureGainUpperLimit` : `float`  
  The largest gain that auto exposure can set.
  - default access: read/write
  - default value: `18.000065071923338`
  - unit: dB
  - default range: 0.0 - 47.994294033026364

`AutoExposureGreyValueLowerLimit` : `float`  
  The lowest value in percentage that the target mean may reach.
  - default access: read/write
  - default value: `3.9100684261974585`
  - unit: %
  - default range: 0.0 - 93.841642228739

`AutoExposureGreyValueUpperLimit` : `float`  
  The highest value in percentage that the target mean may reach.
  - default access: read/write
  - default value: `93.841642228739`
  - unit: %
  - default range: 3.9100684261974585 - 100.0

`AutoExposureLightingMode` : `enum`  
  Selects a lighting mode: Backlight, Frontlight or Normal (default). a. Backlight compensation: used when a strong light is coming from the back of the object. b. Frontlight compensation: used when a strong light is shining in the front of the object while the background is dark. c. Normal lighting: used when the object is not under backlight or frontlight conditions. When normal lighting is selected, metering modes are available.
  - default access: read/write
  - default value: `'Normal'`
  - possible values: `'AutoDetect'`, `'Backlight'`, `'Frontlight'`, `'Normal'`

`AutoExposureMeteringMode` : `enum`  
  Selects a metering mode: average, spot, or partial metering. a. Average: Measures the light from the entire scene uniformly to determine the final exposure value. Every portion of the exposed area has the same contribution. b. Spot: Measures a small area (about 3%) in the center of the scene while the rest of the scene is ignored. This mode is used when the scene has a high contrast and the object of interest is relatively small. c. Partial: Measures the light from a larger area (about 11%) in the center of the scene. This mode is used when very dark or bright regions appear at the edge of the frame. Note: Metering mode is available only when Lighting Mode Selector is Normal.
  - default access: read/write
  - default value: `'Average'`
  - possible values: `'Average'`, `'Spot'`, `'Partial'`, `'CenterWeighted'`, `'HistgramPeak'`

`AutoExposureTargetGreyValue` : `float`  
  This is the user-specified target grey level (image mean) to apply to the current image. Note that the target grey level is in the linear domain before gamma correction is applied.
  - default access: not available
  - unit: %
  - default range: 3.9100684261974585 - 93.841642228739

`AutoExposureTargetGreyValueAuto` : `enum`  
  This indicates whether the target image grey level is automatically set by the camera or manually set by the user. Note that the target grey level is in the linear domain before gamma correction is applied.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values:
    - `'Off'`: Target grey value is manually controlled
    - `'Continuous'`: Target grey value is constantly adapted by the device to maximize the dynamic range.

`BalanceRatio` : `float`  
  Controls the balance ratio of the selected color relative to green. Used for white balancing.
  - default access: read only
  - default value: `1.0986328125`
  - default range: 0.25 - 4.0

`BalanceRatioAddr` : `int`  
  
  - default access: read only
  - default value: `1084416`
  - default range: -9223372036854775808 - 9223372036854775807

`BalanceRatioSelector` : `enum`  
  Selects a balance ratio to configure once a balance ratio control has been selected.
  - default access: read/write
  - default value: `'Red'`
  - possible values:
    - `'Red'`: Selects the red balance ratio control for adjustment.  The red balance ratio is relative to the green channel.
    - `'Blue'`: Selects the blue balance ratio control for adjustment. The blue balance ratio is relative to the green channel.

`BalanceRatioSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`BalanceWhiteAuto` : `enum`  
  White Balance compensates for color shifts caused by different lighting conditions. It can be automatically or manually controlled. For manual control, set to Off. For automatic control, set to Once or Continuous.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values:
    - `'Off'`: Sets operation mode to Off, which is manual control.
    - `'Once'`: Sets operation mode to once. Once runs for a number of iterations and then sets White Balance Auto to Off.
    - `'Continuous'`: Sets operation mode to continuous. Continuous automatically adjusts values if the colors are imbalanced.

`BalanceWhiteAutoDamping` : `float`  
  Controls how quickly 'BalanceWhiteAuto' adjusts the values for Red and Blue BalanceRatio in response to changing conditions.  Higher damping means the changes are more gradual.
  - default access: read/write
  - default value: `0.25`
  - default range: 0.0 - 0.99609375

`BalanceWhiteAutoLowerLimit` : `float`  
  Controls the minimum value Auto White Balance can set for the Red/Blue BalanceRatio.
  - default access: read/write
  - default value: `0.5`
  - default range: 0.25 - 4.0

`BalanceWhiteAutoProfile` : `enum`  
  Selects the profile used by BalanceWhiteAuto.
  - default access: read/write
  - default value: `'Indoor'`
  - possible values:
    - `'Indoor'`: Indoor auto white balance Profile. Can be used to compensate for artificial lighting.
    - `'Outdoor'`: Outdoor auto white balance profile. Designed for scenes with natural lighting.

`BalanceWhiteAutoUpperLimit` : `float`  
  Controls the maximum value Auto White Balance can set the Red/Blue BalanceRatio.
  - default access: read/write
  - default value: `4.0`
  - default range: 0.5 - 4.0

`BinningHorizontal` : `int`  
  Number of horizontal photo-sensitive cells to combine together. This reduces the horizontal resolution (width) of the image. A value of 1 indicates that no horizontal binning is performed by the camera. This value must be 1 for decimation to be active.
  - default access: read/write
  - default value: `1`
  - default range: 1 - 4

`BinningHorizontalMode` : `enum`  
  
  - default access: read/write
  - default value: `'Sum'`
  - possible values:
    - `'Sum'`: The response from the combined horizontal cells is added, resulting in increased sensitivity (a brighter image).
    - `'Average'`: The response from the combined horizontal cells is averaged, resulting in increased signal/noise ratio. Not all sensors support average binning.

`BinningSelector` : `enum`  
  Selects which binning engine is controlled by the BinningHorizontal and BinningVertical features.
  - default access: read/write
  - default value: `'All'`
  - possible values:
    - `'All'`: The total amount of binning to be performed on the captured sensor data.
    - `'Sensor'`: The portion of binning to be performed on the sensor directly.
    - `'ISP'`: The portion of binning to be performed by the image signal processing engine (ISP) outside of the sensor. Note: the ISP can be disabled.

`BinningSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`BinningVertical` : `int`  
  Number of vertical photo-sensitive cells to combine together. This reduces the vertical resolution (height) of the image. A value of 1 indicates that no vertical binning is performed by the camera. This value must be 1 for decimation to be active.
  - default access: read/write
  - default value: `1`
  - default range: 1 - 4

`BinningVerticalMode` : `enum`  
  
  - default access: read/write
  - default value: `'Sum'`
  - possible values:
    - `'Sum'`: The response from the combined vertical cells is added, resulting in increased sensitivity (a brighter image).
    - `'Average'`: The response from the combined vertical cells is averaged, resulting in increased signal/noise ratio. Not all sensors support average binning.

`BlackLevel` : `float`  
  Controls the offset of the video signal in percent.
  - default access: read/write
  - default value: `0.0`
  - unit: %
  - default range: -5.0000011920928955 - 10.000002384185791

`BlackLevelAddr` : `int`  
  
  - default access: read only
  - default value: `1075200`
  - default range: -9223372036854775808 - 9223372036854775807

`BlackLevelClampingEnable` : `bool`  
  Enable the black level auto clamping feature which performing dark current compensation.
  - default access: read/write
  - default value: `True`

`BlackLevelRawAddr` : `int`  
  
  - default access: read only
  - default value: `1074176`
  - default range: -9223372036854775808 - 9223372036854775807

`BlackLevelSelector` : `enum`  
  Selects which black level to control.  Only All can be set by the user. Analog and Digital are read-only.
  - default access: read/write
  - default value: `'All'`
  - possible values: `'All'`, `'Analog'`, `'Digital'`

`BlackLevelSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`ChunkBlackLevel` : `float`  
  Returns the black level used to capture the image.
  - default access: not available
  - unit: %
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`ChunkBlackLevelPercent` : `float`  
  
  - default access: not available
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`ChunkBlackLevelSelector` : `enum`  
  Selects which black level to retrieve
  - default access: read/write
  - default value: `'All'`
  - possible values: `'All'`

`ChunkBlackLevelSelectorInt` : `int`  
  
  - default access: read/write
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`ChunkCRC` : `int`  
  Returns the CRC of the image payload.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkEnable` : `bool`  
  Enables the inclusion of the selected Chunk data in the payload of the image.
  - default access: read/write
  - default value: `False`

`ChunkExposureTime` : `float`  
  Returns the exposure time used to capture the image.
  - default access: not available
  - unit: us
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`ChunkExposureTimeUS` : `float`  
  
  - default access: not available
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`ChunkFrameID` : `int`  
  Returns the image frame ID.
  - default access: not available
  - default range: 0 - 9223372036854775807

`ChunkGain` : `float`  
  Returns the gain used to capture the image.
  - default access: not available
  - unit: dB
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`ChunkGainAddr` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`ChunkGainDB` : `float`  
  
  - default access: not available
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`ChunkGainSelector` : `enum`  
  Selects which gain to retrieve
  - default access: read/write
  - default value: `'All'`
  - possible values: `'All'`, `'Red'`, `'Green'`, `'Blue'`

`ChunkGainSelectorInt` : `int`  
  
  - default access: read/write
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`ChunkHeight` : `int`  
  Returns the height of the image included in the payload.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkImage` : `int`  
  Returns the image payload.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkModeActive` : `bool`  
  Activates the inclusion of Chunk data in the payload of the image.
  - default access: read/write
  - default value: `False`

`ChunkOffsetX` : `int`  
  Returns the Offset X of the image included in the payload.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkOffsetY` : `int`  
  Returns the Offset Y of the image included in the payload.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkPixelFormat` : `enum`  
  Format of the pixel provided by the camera
  - default access: not available
  - possible values: `'Mono8'`, `'Mono12Packed'`, `'Mono16'`, `'RGB8Packed'`, `'YUV422Packed'`, `'BayerGR8'`, `'BayerRG8'`, `'BayerGB8'`, `'BayerBG8'`, `'CbYCrY'`

`ChunkSelector` : `enum`  
  Selects which chunk data to enable or disable.
  - default access: read/write
  - default value: `'FrameID'`
  - possible values: `'Image'`, `'CRC'`, `'FrameID'`, `'OffsetX'`, `'OffsetY'`, `'Width'`, `'Height'`, `'ExposureTime'`, `'Gain'`, `'BlackLevel'`, `'PixelFormat'`, `'Timestamp'`, `'SequencerSetActive'`, `'SerialData'`

`ChunkSequencerSetActive` : `int`  
  Returns the index of the active set of the running sequencer included in the payload.
  - default access: not available
  - default range: -2147483648 - 2147483647

`ChunkSerialData` : `string`  
  Returns the serial data that was received.
  - default access: not available

`ChunkSerialDataLength` : `int`  
  Returns the length of the received serial data that was included in the payload.
  - default access: not available
  - default range: 0 - 4294967295

`ChunkSerialReceiveOverflow` : `bool`  
  Returns the status of the chunk serial receive overflow.
  - default access: not available

`ChunkTimestamp` : `int`  
  Returns the Timestamp of the image.
  - default access: not available
  - default range: 0 - 9223372036854775807

`ChunkWidth` : `int`  
  Returns the width of the image included in the payload.
  - default access: not available
  - default range: 0 - 4294967295

`ColorTransformationEnable` : `bool`  
  Enables/disables the color transform selected with ColorTransformationSelector. For RGB to YUV this is read-only. Enabling/disabling RGB to YUV can only be done by changing pixel format.
  - default access: not available

`ColorTransformationSelector` : `enum`  
  Selects which Color Transformation module is controlled by the various Color Transformation features
  - default access: not available
  - possible values: `'RGBtoRGB'`, `'RGBtoYUV'`

`ColorTransformationValue` : `float`  
  Represents the value of the selected Gain factor or Offset inside the Transformation matrix in floating point precision.
  - default access: not available
  - default range: -32.0 - 31.9990234375

`ColorTransformationValueSelector` : `enum`  
  Selects the Gain factor or Offset of the Transformation matrix to access in the selected Color Transformation module
  - default access: not available
  - possible values: `'Gain00'`, `'Gain01'`, `'Gain02'`, `'Gain10'`, `'Gain11'`, `'Gain12'`, `'Gain20'`, `'Gain21'`, `'Gain22'`, `'Offset0'`, `'Offset1'`, `'Offset2'`

`CounterDelay` : `int`  
  Sets the delay (or number of events) before the CounterStart event is generated.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 65519

`CounterDelayAddr` : `int`  
  
  - default access: read only
  - default value: `919552`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterDuration` : `int`  
  Sets the duration (or number of events) before the CounterEnd event is generated.
  - default access: read/write
  - default value: `1`
  - default range: 1 - 65520

`CounterDurationAddr` : `int`  
  
  - default access: read only
  - default value: `920576`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterEventActivation` : `enum`  
  Selects the activation mode of the event to increment the Counter.
  - default access: not available
  - possible values: `'LevelLow'`, `'LevelHigh'`, `'FallingEdge'`, `'RisingEdge'`, `'AnyEdge'`

`CounterEventActivationAddr` : `int`  
  
  - default access: read only
  - default value: `918528`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterEventSource` : `enum`  
  Selects the event that will increment the counter
  - default access: read/write
  - default value: `'MHzTick'`
  - possible values:
    - `'Off'`: Off
    - `'MHzTick'`: MHzTick
    - `'Line0'`: Line0
    - `'Line1'`: Line1
    - `'Line2'`: Line2
    - `'Line3'`: Line3
    - `'UserOutput0'`: UserOutput0
    - `'UserOutput1'`: UserOutput1
    - `'UserOutput2'`: UserOutput2
    - `'UserOutput3'`: UserOutput3
    - `'Counter0Start'`: Counter0Start
    - `'Counter1Start'`: Counter1Start
    - `'Counter0End'`: Counter0End
    - `'Counter1End'`: Counter1End
    - `'LogicBlock0'`: LogicBlock0
    - `'LogicBlock1'`: LogicBlock1
    - `'ExposureStart'`: ExposureStart
    - `'ExposureEnd'`: ExposureEnd
    - `'FrameTriggerWait'`: FrameTriggerWait

`CounterEventSourceAddr` : `int`  
  
  - default access: read only
  - default value: `917504`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterResetActivation` : `enum`  
  Selects the Activation mode of the Counter Reset Source signal.
  - default access: not available
  - possible values: `'LevelLow'`, `'LevelHigh'`, `'FallingEdge'`, `'RisingEdge'`, `'AnyEdge'`

`CounterResetActivationAddr` : `int`  
  
  - default access: read only
  - default value: `925696`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterResetSource` : `enum`  
  Selects the signal that will be the source to reset the Counter.
  - default access: not available
  - possible values:
    - `'Off'`: Off
    - `'Line0'`: Line0
    - `'Line1'`: Line1
    - `'Line2'`: Line2
    - `'Line3'`: Line3
    - `'UserOutput0'`: UserOutput0
    - `'UserOutput1'`: UserOutput1
    - `'UserOutput2'`: UserOutput2
    - `'UserOutput3'`: UserOutput3
    - `'Counter0Start'`: Counter0Start
    - `'Counter1Start'`: Counter1Start
    - `'Counter0End'`: Counter0End
    - `'Counter1End'`: Counter1End
    - `'LogicBlock0'`: LogicBlock0
    - `'LogicBlock1'`: LogicBlock1
    - `'ExposureStart'`: ExposureStart
    - `'ExposureEnd'`: ExposureEnd
    - `'FrameTriggerWait'`: FrameTriggerWait

`CounterResetSourceAddr` : `int`  
  
  - default access: read only
  - default value: `924672`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterSelector` : `enum`  
  Selects which counter to configure
  - default access: read/write
  - default value: `'Counter0'`
  - possible values: `'Counter0'`, `'Counter1'`

`CounterSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterStatus` : `enum`  
  Returns the current status of the Counter.
  - default access: read only
  - default value: `'CounterTriggerWait'`
  - possible values:
    - `'CounterIdle'`: The counter is idle.
    - `'CounterTriggerWait'`: The counter is waiting for a start trigger.
    - `'CounterActive'`: The counter is counting for the specified duration.
    - `'CounterCompleted'`: The counter reached the CounterDuration count.
    - `'CounterOverflow'`: The counter reached its maximum possible count.

`CounterStatusAddr` : `int`  
  
  - default access: read only
  - default value: `927744`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterTriggerActivation` : `enum`  
  Selects the activation mode of the trigger to start the Counter.
  - default access: read/write
  - default value: `'RisingEdge'`
  - possible values: `'LevelLow'`, `'LevelHigh'`, `'FallingEdge'`, `'RisingEdge'`, `'AnyEdge'`

`CounterTriggerActivationAddr` : `int`  
  
  - default access: read only
  - default value: `923648`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterTriggerSource` : `enum`  
  Selects the source of the trigger to start the counter
  - default access: read/write
  - default value: `'ExposureStart'`
  - possible values:
    - `'Off'`: Off
    - `'Line0'`: Line0
    - `'Line1'`: Line1
    - `'Line2'`: Line2
    - `'Line3'`: Line3
    - `'UserOutput0'`: UserOutput0
    - `'UserOutput1'`: UserOutput1
    - `'UserOutput2'`: UserOutput2
    - `'UserOutput3'`: UserOutput3
    - `'Counter0Start'`: Counter0Start
    - `'Counter1Start'`: Counter1Start
    - `'Counter0End'`: Counter0End
    - `'Counter1End'`: Counter1End
    - `'LogicBlock0'`: LogicBlock0
    - `'LogicBlock1'`: LogicBlock1
    - `'ExposureStart'`: ExposureStart
    - `'ExposureEnd'`: ExposureEnd
    - `'FrameTriggerWait'`: FrameTriggerWait

`CounterTriggerSourceAddr` : `int`  
  
  - default access: read only
  - default value: `922624`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterValue` : `int`  
  Current counter value
  - default access: read only
  - default value: `1`
  - default range: 0 - 65535

`CounterValueAddr` : `int`  
  
  - default access: read only
  - default value: `921600`
  - default range: -9223372036854775808 - 9223372036854775807

`CounterValueAtReset` : `int`  
  Value of the selected Counter when it was reset by a trigger.
  - default access: not available
  - default range: 0 - 65535

`CounterValueAtResetAddr` : `int`  
  
  - default access: read only
  - default value: `926720`
  - default range: -9223372036854775808 - 9223372036854775807

`DecimationHorizontal` : `int`  
  Horizontal decimation of the image.  This reduces the horizontal resolution (width) of the image by only retaining a single pixel within a window whose size is the decimation factor specified here. A value of 1 indicates that no horizontal decimation is performed by the camera. This value must be 1 for binning to be active.
  - default access: read/write
  - default value: `1`
  - default range: 1 - 2

`DecimationHorizontalMode` : `enum`  
  The mode used to reduce the horizontal resolution when DecimationHorizontal is used. The current implementation only supports a single decimation mode: Discard.  Average should be achieved via Binning.
  - default access: read/write
  - default value: `'Discard'`
  - possible values:
    - `'Discard'`: The value of every Nth pixel is kept, others are discarded.

`DecimationSelector` : `enum`  
  Selects which decimation layer is controlled by the DecimationHorizontal and DecimationVertical features.
  - default access: read/write
  - default value: `'All'`
  - possible values:
    - `'All'`: The total amount of decimation to be performed on the captured image data.
    - `'Sensor'`: The portion of decimation to be performed on the sensor directly. Currently this is the only decimation layer available and hence is identical to the "All" layer.  All decimation modification should therefore be done via the "All" layer only.

`DecimationSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`DecimationVertical` : `int`  
  Vertical decimation of the image.  This reduces the vertical resolution (height) of the image by only retaining a single pixel within a window whose size is the decimation factor specified here. A value of 1 indicates that no vertical decimation is performed by the camera. This value must be 1 for binning to be active.
  - default access: read/write
  - default value: `1`
  - default range: 1 - 2

`DecimationVerticalMode` : `enum`  
  The mode used to reduce the vertical resolution when DecimationVertical is used. The current implementation only supports a single decimation mode: Discard.  Average should be achieved via Binning.
  - default access: read/write
  - default value: `'Discard'`
  - possible values:
    - `'Discard'`: The value of every Nth pixel is kept, others are discarded.

`DefectCorrectStaticEnable` : `bool`  
  Enables/Disables table-based defective pixel correction.
  - default access: read/write
  - default value: `True`

`DefectCorrectionMode` : `enum`  
  Controls the method used for replacing defective pixels.
  - default access: read/write
  - default value: `'Average'`
  - possible values:
    - `'Average'`: Pixels are replaced with the average of their neighbours.  This is the normal mode of operation.
    - `'Highlight'`: Pixels are replaced with the maximum pixel value (i.e., 255 for 8-bit images).  Can be used for debugging the table.
    - `'Zero'`: Pixels are replaced by the value zero.  Can be used for testing the table.

`DefectTableCoordinateX` : `int`  
  Returns the X coordinate of the defective pixel at DefectTableIndex within the defective pixel table. Changes made do not take effect in captured images until the command DefectTableApply is written.
  - default access: read/write
  - default value: `221`
  - default range: 0 - 4095

`DefectTableCoordinateY` : `int`  
  Returns the Y coordinate of the defective pixel at DefectTableIndex within the defective pixel table. Changes made do not take effect in captured images until the command DefectTableApply is written.
  - default access: read/write
  - default value: `1243`
  - default range: 0 - 2999

`DefectTableIndex` : `int`  
  Controls the offset of the element to access in the defective pixel location table.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 21

`DefectTablePixelCount` : `int`  
  The number of defective pixel locations in the current table.
  - default access: read/write
  - default value: `22`
  - default range: 0 - 255

`DeviceFirmwareVersion` : `string`  
  Firmware version of the device.
  - default access: read only
  - default value: `'1707.1.4.0'`

`DeviceGenCPVersionMajor` : `int`  
  Major version of the GenCP protocol supported by the device.
  - default access: read only
  - default value: `1`
  - default range: 0 - 65535

`DeviceGenCPVersionMinor` : `int`  
  Minor version of the GenCP protocol supported by the device.
  - default access: read only
  - default value: `0`
  - default range: 0 - 65535

`DeviceID` : `string`  
  Device identifier (serial number).
  - default access: read only
  - default value: `'19290166'`

`DeviceIndicatorMode` : `enum`  
  Controls the LED behaviour: Inactive (off), Active (current status), or Error Status (off unless an error occurs).
  - default access: read/write
  - default value: `'Active'`
  - possible values: `'Inactive'`, `'Active'`, `'ErrorStatus'`

`DeviceLinkBandwidthReserve` : `float`  
  Percentage of streamed data bandwidth reserved for packet resend.
  - default access: read/write
  - default value: `0.0`
  - unit: %
  - default range: 0.0 - 0.0

`DeviceLinkCurrentThroughput` : `int`  
  Current bandwidth of streamed data.
  - default access: read only
  - default value: `378171580`
  - unit: Bps
  - default range: 0 - 4294967295

`DeviceLinkSpeed` : `int`  
  Link Speed
  - default access: read only
  - default value: `500000000`
  - default range: 0 - 4294967295

`DeviceLinkThroughputLimit` : `int`  
  Limits the maximum bandwidth of the data that will be streamed out by the device on the selected Link. If necessary, delays will be uniformly inserted between transport layer packets in order to control the peak bandwidth.
  - default access: read/write
  - default value: `380000000`
  - unit: Bps
  - default range: 0 - 500000000

`DeviceManufacturerInfo` : `string`  
  Additional manufacturer info.
  - default access: read only
  - default value: `'Aug 28 2017 12:12:28'`

`DeviceMaxThroughput` : `int`  
  Maximum bandwidth of the data that can be streamed out of the device. This can be used to estimate if the physical connection(s) can sustain transfer of free-running images from the camera at its maximum speed.
  - default access: read only
  - default value: `391395227`
  - unit: Bps
  - default range: 0 - 4294967295

`DeviceModelName` : `string`  
  Model name of the device.
  - default access: read only
  - default value: `'Blackfly S BFS-U3-123S6C'`

`DevicePowerSupplySelector` : `enum`  
  Selects the power supply source to control or read.
  - default access: read/write
  - default value: `'External'`
  - possible values: `'External'`

`DevicePowerSupplySelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`DeviceScanType` : `enum`  
  Scan type of the sensor of the device.
  - default access: read only
  - default value: `'Areascan'`
  - possible values: `'Areascan'`

`DeviceSerialNumber` : `string`  
  Device serial number. This string is a unique identifier of the device.
  - default access: read only
  - default value: `'19290166'`

`DeviceTLType` : `enum`  
  Transport Layer type of the device.
  - default access: read only
  - default value: `'USB3Vision'`
  - possible values: `'GigEVision'`, `'CameraLink'`, `'CameraLinkHS'`, `'CoaXPress'`, `'USB3Vision'`, `'Custom'`

`DeviceTemperature` : `float`  
  Device temperature in degrees Celsius (C).
  - default access: read only
  - default value: `52.125`
  - unit: C
  - default range: -125.0 - 125.0

`DeviceTemperatureAddr` : `int`  
  
  - default access: read only
  - default value: `266240`
  - default range: -9223372036854775808 - 9223372036854775807

`DeviceTemperatureSelector` : `enum`  
  Selects the location within the device, where the temperature will be measured.
  - default access: read/write
  - default value: `'Sensor'`
  - possible values: `'Sensor'`

`DeviceTemperatureSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`DeviceUptime` : `int`  
  Total time since the device was powered up in seconds.
  - default access: read only
  - default value: `4`
  - unit: s
  - default range: 0 - 4294967295

`DeviceUserID` : `string`  
  User Defined Name. This can be used to enter a unique device name. This information is retained over power cycles.
  - default access: read/write
  - default value: `''`

`DeviceVendorName` : `string`  
  Name of the manufacturer of the device.
  - default access: read only
  - default value: `'FLIR'`

`DeviceVersion` : `string`  
  Version of the device.
  - default access: read only
  - default value: `'1707.1.4.0'`

`EnumerationCount` : `int`  
  Number of enumerations since uptime.
  - default access: read only
  - default value: `1`
  - default range: 0 - 4294967295

`EvCompensationRaw` : `int`  
  The EV compensation value used in the exposure compensation in device unit
  - default access: read/write
  - default value: `32`
  - default range: 23 - 41

`EventError` : `int`  
  Returns the unique identifier of the Error type of Event.
  - default access: read only
  - default value: `40000`
  - default range: -9223372036854775808 - 9223372036854775807

`EventErrorCode` : `int`  
  Returns the error code for the error that happened.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventErrorFrameID` : `int`  
  Returns the unique identifier of the frame (or image) that generated the Error Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventErrorTimestamp` : `int`  
  Returns the Timestamp of the Error Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventExposureEnd` : `int`  
  Returns the unique identifier of the Exposure End type of Event.
  - default access: read only
  - default value: `40003`
  - default range: -9223372036854775808 - 9223372036854775807

`EventExposureEndFrameID` : `int`  
  Returns the unique identifier of the frame (or image) that generated the Exposure End Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventExposureEndTimestamp` : `int`  
  Returns the Timestamp of the Exposure End Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventNotification` : `enum`  
  Enables/Disables the selected event.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'On'`, `'Off'`

`EventNotificationAddr` : `int`  
  
  - default access: read only
  - default value: `1318912`
  - default range: -9223372036854775808 - 9223372036854775807

`EventSelector` : `enum`  
  Selects which Event to enable or disable.
  - default access: read/write
  - default value: `'Error'`
  - possible values: `'Error'`, `'ExposureEnd'`, `'SerialPortReceive'`

`EventSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`EventSerialData` : `string`  
  Returns the serial data that was received.
  - default access: not available

`EventSerialDataLength` : `int`  
  Returns the length of the received serial data that was included in the event payload.
  - default access: not available
  - default range: 0 - 4294967295

`EventSerialPortReceive` : `int`  
  Returns the unique identifier of the Serial Port Receive type of Event.
  - default access: read only
  - default value: `40005`
  - default range: -9223372036854775808 - 9223372036854775807

`EventSerialPortReceiveTimestamp` : `int`  
  Returns the Timestamp of the Serial Port Receive Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`EventSerialReceiveOverflow` : `bool`  
  Returns the status of the event serial receive overflow.
  - default access: not available

`EventTest` : `int`  
  Returns the unique identifier of the Test type of Event.
  - default access: read only
  - default value: `20479`
  - default range: -9223372036854775808 - 9223372036854775807

`EventTestTimestamp` : `int`  
  Returns the Timestamp of the Test Event.
  - default access: not available
  - default range: 0 - 9223372036854775807

`ExposureAuto` : `enum`  
  Sets the automatic exposure mode
  - default access: read/write
  - default value: `'Continuous'`
  - possible values:
    - `'Off'`: Exposure time is manually controlled using ExposureTime
    - `'Once'`: Exposure time is adapted once by the device. Once it has converged, it returns to the Off state.
    - `'Continuous'`: Exposure time is constantly adapted by the device to maximize the dynamic range.

`ExposureMode` : `enum`  
  Sets the operation mode of the Exposure.
  - default access: read/write
  - default value: `'Timed'`
  - possible values:
    - `'Timed'`: Timed exposure. The exposure time is set using the ExposureTime or ExposureAuto features and the exposure starts with the FrameStart or LineStart.
    - `'TriggerWidth'`: Uses the width of the current Frame trigger signal pulse to control the exposure time.

`ExposureTime` : `float`  
  Exposure time in microseconds when Exposure Mode is Timed.
  - default access: read only
  - default value: `995.0`
  - unit: us
  - default range: 10.0 - 30000004.0

`ExposureTimeRaw` : `int`  
  
  - default access: read only
  - default value: `97`
  - default range: 1 - 2923977

`FfcEnable` : `bool`  
  Enable or disable flat field correction.
  - default access: not available

`FfcMode` : `enum`  
  Selects flat field correction mode. Note that flat field correction parameters are accessible only in Calibration mode. When switching modes from Calibration to User or Factory, it is recommended to stop image streaming to give the camera enough time to load the corresponding table.
  - default access: not available
  - possible values: `'Factory'`, `'User'`, `'Calibration'`

`FfcUserGain` : `float`  
  The value of user flat field gain correction for the current pixel.
  - default access: not available
  - default range: 1.0 - 1.2490234375

`FfcUserOffset` : `int`  
  The value of user flat field offset correction for the current pixel.
  - default access: not available
  - default range: -4096 - 4064

`FfcUserTableXCoordinate` : `int`  
  Controls the pixel X coordinate of the user flat field correction coefficients.
  - default access: not available
  - default range: 0 - 4095

`FileAccessLength` : `int`  
  Controls the Length of the mapping between the device file storage and the FileAccessBuffer.
  - default access: read/write
  - default value: `1`
  - unit: B
  - default range: 0 - 4096

`FileAccessOffset` : `int`  
  Controls the Offset of the mapping between the device file storage and the FileAccessBuffer.
  - default access: read/write
  - default value: `0`
  - unit: B
  - default range: 0 - 8388608

`FileOpenMode` : `enum`  
  The mode of the file when it is opened. The file can be opened for reading, writting or both. This must be set before opening the file.
  - default access: read/write
  - default value: `'Read'`
  - possible values: `'Read'`, `'Write'`, `'ReadWrite'`

`FileOperationResult` : `int`  
  Represents the file operation result. For Read or Write operations, the number of successfully read/written bytes is returned.
  - default access: read only
  - default value: `0`
  - default range: 0 - 4294967295

`FileOperationSelector` : `enum`  
  Sets operation to execute on the selected file when the execute command is given.
  - default access: read/write
  - default value: `'Open'`
  - possible values: `'Open'`, `'Close'`, `'Read'`, `'Write'`, `'Delete'`

`FileOperationStatus` : `enum`  
  Represents the file operation execution status.
  - default access: read only
  - default value: `'Success'`
  - possible values:
    - `'Success'`: File Operation was sucessful.
    - `'Failure'`: File Operation failed.
    - `'Overflow'`: An overflow occurred while executing the File Operation.

`FileSelector` : `enum`  
  Selects which file is being operated on. This must be set before performing any file operations.
  - default access: read/write
  - default value: `'UserSetDefault'`
  - possible values: `'UserSetDefault'`, `'UserSet0'`, `'UserSet1'`, `'UserFile1'`, `'SerialPort0'`

`FileSize` : `int`  
  Represents the size of the selected file in bytes.
  - default access: read only
  - default value: `1368`
  - unit: B
  - default range: 0 - 4294967295

`Gain` : `float`  
  Controls the amplification of the video signal in dB.
  - default access: read only
  - default value: `0.0`
  - unit: dB
  - default range: 0.0 - 47.994294033026364

`GainAddr` : `int`  
  
  - default access: read only
  - default value: `1067008`
  - default range: -9223372036854775808 - 9223372036854775807

`GainAuto` : `enum`  
  Sets the automatic gain mode. Set to Off for manual control. Set to Once for a single automatic adjustment then return to Off. Set to Continuous for constant adjustment. In automatic modes, the camera adjusts the gain to maximize the dynamic range.
  - default access: read/write
  - default value: `'Continuous'`
  - possible values:
    - `'Off'`: Gain is manually controlled
    - `'Once'`: Gain is adapted once by the device. Once it has converged, it returns to the Off state.
    - `'Continuous'`: Gain is constantly adapted by the device to maximize the dynamic range.

`GainRaw` : `int`  
  Controls the amplification of the video signal in camera specific units
  - default access: read only
  - default value: `0`
  - default range: 0 - 480

`GainRawAddr` : `int`  
  
  - default access: read only
  - default value: `1065984`
  - default range: -9223372036854775808 - 9223372036854775807

`GainSelector` : `enum`  
  Selects which gain to control. The All selection is a total amplification across all channels (or taps).
  - default access: read/write
  - default value: `'All'`
  - possible values: `'All'`

`GainSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`Gamma` : `float`  
  Controls the gamma correction of pixel intensity.
  - default access: read/write
  - default value: `0.800048828125`
  - default range: 0.25 - 4.0

`GammaEnable` : `bool`  
  Enables/disables gamma correction.
  - default access: read/write
  - default value: `True`

`GuiXmlManifestAddress` : `int`  
  Location of the GUI XML manifest table.
  - default access: read only
  - default value: `4026535968`
  - default range: 0 - 4294967295

`HbinAddr` : `int`  
  
  - default access: read only
  - default value: `543744`
  - default range: -9223372036854775808 - 9223372036854775807

`HdecAddr` : `int`  
  
  - default access: read only
  - default value: `544768`
  - default range: -9223372036854775808 - 9223372036854775807

`Height` : `int`  
  Height of the image provided by the device (in pixels).
  - default access: read/write
  - default value: `3000`
  - default range: 6 - 3000

`HeightMax` : `int`  
  Maximum height of the image (in pixels). This dimension is calculated after vertical binning. HeightMax does not take into account the current Region of interest (Height or OffsetY).
  - default access: read only
  - default value: `3000`
  - default range: 0 - 4294967295

`IspEnable` : `bool`  
  Controls whether the image processing core is used for optional pixel format mode (i.e. mono).
  - default access: read/write
  - default value: `False`

`LUTEnable` : `bool`  
  Activates the selected LUT.
  - default access: read/write
  - default value: `False`

`LUTIndex` : `int`  
  Control the index (offset) of the coefficient to access in the selected LUT.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 2047

`LUTSelector` : `enum`  
  Selects which LUT to control.
  - default access: read/write
  - default value: `'LUT1'`
  - possible values:
    - `'LUT1'`: This LUT is for re-mapping pixels of all formats (mono, Bayer, red, green and blue).

`LUTValue` : `int`  
  Returns the Value at entry LUTIndex of the LUT selected by LUTSelector.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 511

`LineFilterWidth` : `float`  
  Filter width in microseconds for the selected line and filter combination
  - default access: read/write
  - default value: `0.0`
  - unit: us
  - default range: 0.0 - 104856.0

`LineFilterWidthAddr` : `int`  
  
  - default access: read only
  - default value: `856064`
  - default range: -9223372036854775808 - 9223372036854775807

`LineFormat` : `enum`  
  Displays the current electrical format of the selected physical input or output Line.
  - default access: read only
  - default value: `'OptoCoupled'`
  - possible values: `'NoConnect'`, `'TriState'`, `'TTL'`, `'LVDS'`, `'RS422'`, `'OptoCoupled'`, `'OpenDrain'`

`LineFormatAddr` : `int`  
  
  - default access: read only
  - default value: `852992`
  - default range: -9223372036854775808 - 9223372036854775807

`LineInputFilterSelector` : `enum`  
  Selects the kind of input filter to configure: Deglitch or Debounce.
  - default access: read/write
  - default value: `'Deglitch'`
  - possible values: `'Deglitch'`, `'Debounce'`

`LineInputFilterSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`LineInverter` : `bool`  
  Controls the inversion of the signal of the selected input or output line.
  - default access: read/write
  - default value: `False`

`LineInverterAddr` : `int`  
  
  - default access: read only
  - default value: `854016`
  - default range: -9223372036854775808 - 9223372036854775807

`LineMode` : `enum`  
  Controls if the physical Line is used to Input or Output a signal.
  - default access: read/write
  - default value: `'Input'`
  - possible values: `'Input'`, `'Output'`

`LineModeAddr` : `int`  
  
  - default access: read only
  - default value: `851968`
  - default range: -9223372036854775808 - 9223372036854775807

`LineSelector` : `enum`  
  Selects the physical line (or pin) of the external device connector to configure
  - default access: read/write
  - default value: `'Line0'`
  - possible values: `'Line0'`, `'Line1'`, `'Line2'`, `'Line3'`

`LineSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`LineSource` : `enum`  
  Selects which internal acquisition or I/O source signal to output on the selected line. LineMode must be Output.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'Off'`, `'Line0'`, `'Line1'`, `'Line2'`, `'Line3'`, `'UserOutput0'`, `'UserOutput1'`, `'UserOutput2'`, `'UserOutput3'`, `'Counter0Active'`, `'Counter1Active'`, `'LogicBlock0'`, `'LogicBlock1'`, `'ExposureActive'`, `'FrameTriggerWait'`, `'PPSSignal'`, `'SerialPort0'`

`LineSourceAddr` : `int`  
  
  - default access: read only
  - default value: `857088`
  - default range: -9223372036854775808 - 9223372036854775807

`LineStatus` : `bool`  
  Returns the current status of the selected input or output Line
  - default access: read only
  - default value: `False`

`LineStatusAll` : `int`  
  Returns the current status of all the line status bits in a hexadecimal representation (Line 0 status corresponds to bit 0, Line 1 status with bit 1, etc). This allows simultaneous reading of all line statuses at once.
  - default access: read only
  - default value: `12`
  - default range: 0 - 15

`LinkErrorCount` : `int`  
  Counts the number of error on the link.
  - default access: read only
  - default value: `0`
  - default range: 0 - 4294967295

`LinkRecoveryCount` : `int`  
  Counts the number of times the USB link has recovered.
  - default access: read only
  - default value: `0`
  - default range: 0 - 4294967295

`LinkUptime` : `int`  
  Time since the last phy negotiation (enumeration).
  - default access: read only
  - default value: `1`
  - unit: s
  - default range: 0 - 4294967295

`LogicBlockLUTInputActivation` : `enum`  
  Selects the activation mode of the Logic Input Source signal.
  - default access: read/write
  - default value: `'LevelHigh'`
  - possible values: `'LevelLow'`, `'LevelHigh'`, `'FallingEdge'`, `'RisingEdge'`, `'AnyEdge'`

`LogicBlockLUTInputSelector` : `enum`  
  Controls which LogicBlockLUT Input Source & Activation to access.
  - default access: read/write
  - default value: `'Input0'`
  - possible values: `'Input0'`, `'Input1'`, `'Input2'`, `'Input3'`

`LogicBlockLUTInputSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`LogicBlockLUTInputSource` : `enum`  
  Selects the source for the input into the Logic LUT.
  - default access: read/write
  - default value: `'Zero'`
  - possible values:
    - `'Zero'`: Zero
    - `'Line0'`: Line0
    - `'Line1'`: Line1
    - `'Line2'`: Line2
    - `'Line3'`: Line3
    - `'UserOutput0'`: UserOutput0
    - `'UserOutput1'`: UserOutput1
    - `'UserOutput2'`: UserOutput2
    - `'UserOutput3'`: UserOutput3
    - `'Counter0Start'`: Counter0Start
    - `'Counter1Start'`: Counter1Start
    - `'Counter0End'`: Counter0End
    - `'Counter1End'`: Counter1End
    - `'LogicBlock0'`: LogicBlock0
    - `'LogicBlock1'`: LogicBlock1
    - `'ExposureStart'`: ExposureStart
    - `'ExposureEnd'`: ExposureEnd
    - `'FrameTriggerWait'`: FrameTriggerWait
    - `'AcquisitionActive'`: AcquisitionActive

`LogicBlockLUTOutputValue` : `bool`  
  Controls the output column of the truth table for the selected LogicBlockLUTRowIndex.
  - default access: read/write
  - default value: `True`

`LogicBlockLUTOutputValueAll` : `int`  
  Sets the value of all the output bits in the selected LUT.
  - default access: read/write
  - default value: `255`
  - default range: 0 - 255

`LogicBlockLUTRowIndex` : `int`  
  Controls the row of the truth table to access in the selected LUT.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 7

`LogicBlockLUTSelector` : `enum`  
  Selects which LogicBlock LUT to configure
  - default access: read/write
  - default value: `'Value'`
  - possible values: `'Value'`, `'Enable'`

`LogicBlockLUTSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`LogicBlockSelector` : `enum`  
  Selects which LogicBlock to configure
  - default access: read/write
  - default value: `'LogicBlock0'`
  - possible values: `'LogicBlock0'`, `'LogicBlock1'`

`LogicBlockSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`MaxDeviceResetTime` : `int`  
  Time to wait until device reset complete (ms).
  - default access: read only
  - default value: `30000`
  - unit: ms
  - default range: 0 - 4294967295

`OffsetX` : `int`  
  Horizontal offset from the origin to the ROI (in pixels).
  - default access: read/write
  - default value: `0`
  - default range: 0 - 0

`OffsetY` : `int`  
  Vertical offset from the origin to the ROI (in pixels).
  - default access: read/write
  - default value: `0`
  - default range: 0 - 0

`PayloadSize` : `int`  
  Provides the number of bytes transferred for each image or chunk on the stream channel.
  - default access: read only
  - default value: `12288000`
  - default range: 0 - 4294967295

`PixelColorFilter` : `enum`  
  Type of color filter that is applied to the image. Only applies to Bayer pixel formats. All others have no color filter.
  - default access: read only
  - default value: `'BayerRG'`
  - possible values:
    - `'None'`: No color filter.
    - `'BayerRG'`: Bayer Red Green filter.
    - `'BayerGB'`: Bayer Green Blue filter.
    - `'BayerGR'`: Bayer Green Red filter.
    - `'BayerBG'`: Bayer Blue Green filter.

`PixelDynamicRangeMax` : `int`  
  Maximum value that can be returned during the digitization process. This corresponds to the brightest value of the camera. For color cameras, this returns the biggest value that each color component can take.
  - default access: read only
  - default value: `255`
  - default range: -9223372036854775808 - 9223372036854775807

`PixelDynamicRangeMin` : `int`  
  Minimum value that can be returned during the digitization process. This corresponds to the darkest value of the camera. For color cameras, this returns the smallest value that each color component can take.
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`PixelFormat` : `enum`  
  Format of the pixel provided by the camera.
  - default access: read/write
  - default value: `'BayerRG8'`
  - possible values: `'Mono8'`, `'Mono16'`, `'RGB8Packed'`, `'BayerGR8'`, `'BayerRG8'`, `'BayerGB8'`, `'BayerBG8'`, `'BayerGR16'`, `'BayerRG16'`, `'BayerGB16'`, `'BayerBG16'`, `'Mono10Packed'`, `'BayerGR10Packed'`, `'BayerRG10Packed'`, `'BayerGB10Packed'`, `'BayerBG10Packed'`, `'Mono12Packed'`, `'BayerGR12Packed'`, `'BayerRG12Packed'`, `'BayerGB12Packed'`, `'BayerBG12Packed'`, `'YUV411Packed'`, `'YUV422Packed'`, `'YUV444Packed'`, `'Mono10p'`, `'BayerGR10p'`, `'BayerRG10p'`, `'BayerGB10p'`, `'BayerBG10p'`, `'Mono12p'`, `'BayerGR12p'`, `'BayerRG12p'`, `'BayerGB12p'`, `'BayerBG12p'`, `'YCbCr8'`, `'8'`, `'8'`, `'BGR8'`, `'BGRa8'`

`PixelSize` : `enum`  
  Total size in bits of a pixel of the image.
  - default access: read only
  - default value: `'Bpp8'`
  - possible values:
    - `'Bpp1'`: 1 bit per pixel.
    - `'Bpp2'`: 2 bits per pixel.
    - `'Bpp4'`: 4 bits per pixel.
    - `'Bpp8'`: 8 bits per pixel.
    - `'Bpp10'`: 10 bits per pixel.
    - `'Bpp12'`: 12 bits per pixel.
    - `'Bpp14'`: 14 bits per pixel.
    - `'Bpp16'`: 16 bits per pixel.
    - `'Bpp20'`: 20 bits per pixel.
    - `'Bpp24'`: 24 bits per pixel.
    - `'Bpp30'`: 30 bits per pixel.
    - `'Bpp32'`: 32 bits per pixel.
    - `'Bpp36'`: 36 bits per pixel.
    - `'Bpp48'`: 48 bits per pixel.
    - `'Bpp64'`: 64 bits per pixel.
    - `'Bpp96'`: 96 bits per pixel.

`PowerSupplyCurrent` : `float`  
  Indicates the output current of the selected power supply (A).
  - default access: read only
  - default value: `0.5908203125`
  - unit: A
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`PowerSupplyCurrentAddr` : `int`  
  
  - default access: read only
  - default value: `268288`
  - default range: -9223372036854775808 - 9223372036854775807

`PowerSupplyVoltage` : `float`  
  Indicates the current voltage of the selected power supply (V).
  - default access: read only
  - default value: `4.765380859375`
  - unit: V
  - default range: -1.7976931348623157e+308 - 1.7976931348623157e+308

`PowerSupplyVoltageAddr` : `int`  
  
  - default access: read only
  - default value: `267264`
  - default range: -9223372036854775808 - 9223372036854775807

`ReverseX` : `bool`  
  Horizontally flips the image sent by the device. The region of interest is applied after flipping. For color cameras the bayer pixel format is affected. For example, BayerRG16 changes to BayerGR16.
  - default access: read/write
  - default value: `False`

`ReverseY` : `bool`  
  Vertically flips the image sent by the device. The region of interest is applied after flipping. For color cameras the bayer pixel format is affected. For example, BayerRG16 changes to BayerGB16.
  - default access: read/write
  - default value: `False`

`RgbTransformLightSource` : `enum`  
  Used to select from a set of RGBtoRGB transform matricies calibrated for different light sources. Selecting a value also sets the white balance ratios (BalanceRatioRed and BalanceRatioBlue), but those can be overwritten through manual or auto white balance.
  - default access: read/write
  - default value: `'General'`
  - possible values:
    - `'General'`: Uses a matrix calibrated for a wide range of light sources.
    - `'Tungsten2800K'`: Uses a matrix optimized for tungsten/incandescent light with color temperature 2800K.
    - `'WarmFluorescent3000K'`: Uses a matrix optimized for a typical warm fluoresecent light with color temperature 3000K.
    - `'CoolFluorescent4000K'`: Uses a matrix optimized for a typical cool fluoresecent light with color temperature 4000K.
    - `'Daylight5000K'`: Uses a matrix optimized for noon Daylight with color temperature 5000K.
    - `'Cloudy6500K'`: Uses a matrix optimized for a cloudy sky with color temperature 6500K.
    - `'Shade8000K'`: Uses a matrix optimized for shade with color temperature 8000K.
    - `'Custom'`: Uses a custom matrix set by the user through the ColorTransformationValueSelector and ColorTransformationValue controls.

`Saturation` : `float`  
  Controls the color saturation.
  - default access: not available
  - default range: 0.0 - 3.9990234375

`SaturationEnable` : `bool`  
  Enables/disables Saturation adjustment.
  - default access: not available

`SensorDescription` : `string`  
  Returns Sensor Description
  - default access: read only
  - default value: `'Sony IMX253 (1.1" Color CMOS)'`

`SensorHeight` : `int`  
  Effective height of the sensor in pixels.
  - default access: read only
  - default value: `3008`
  - default range: -9223372036854775808 - 9223372036854775807

`SensorShutterMode` : `enum`  
  Sets the shutter mode of the device.
  - default access: read/write
  - default value: `'Global'`
  - possible values:
    - `'Global'`: The shutter opens and closes at the same time for all pixels. All the pixels are exposed for the same length of time at the same time.
    - `'Rolling'`: The shutter opens and closes sequentially for groups (typically lines) of pixels. All the pixels are exposed for the same length of time but not at the same time.
    - `'GlobalReset'`: The shutter opens at the same time for all pixels but ends in a sequential manner. The pixels are exposed for different lengths of time.

`SensorWidth` : `int`  
  Effective width of the sensor in pixels.
  - default access: read only
  - default value: `4112`
  - default range: -9223372036854775808 - 9223372036854775807

`SequencerConfigurationMode` : `enum`  
  Controls whether or not a sequencer is in configuration mode.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'Off'`, `'On'`

`SequencerConfigurationValid` : `enum`  
  Display whether the current sequencer configuration is valid to run.
  - default access: read only
  - default value: `'No'`
  - possible values: `'No'`, `'Yes'`

`SequencerFeatureEnable` : `bool`  
  Enables the selected feature and makes it active in all sequencer sets.
  - default access: read/write
  - default value: `True`

`SequencerFeatureSelector` : `enum`  
  Selects which sequencer features to control.
  - default access: read/write
  - default value: `'ExposureTime'`
  - possible values: `'ExposureTime'`, `'Gain'`

`SequencerMode` : `enum`  
  Controls whether or not a sequencer is active.
  - default access: read only
  - default value: `'Off'`
  - possible values: `'Off'`, `'On'`

`SequencerPathSelector` : `int`  
  Selects branching path to be used for subsequent settings.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 0

`SequencerSetActive` : `int`  
  Displays the currently active sequencer set.
  - default access: not available
  - default range: 0 - 7

`SequencerSetNext` : `int`  
  Specifies the next sequencer set.
  - default access: not available
  - default range: 0 - 7

`SequencerSetSelector` : `int`  
  Selects the sequencer set to which subsequent settings apply.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 7

`SequencerSetStart` : `int`  
  Sets the first sequencer set to be used.
  - default access: read only
  - default value: `0`
  - default range: 0 - 7

`SequencerSetValid` : `enum`  
  Displays whether the currently selected sequencer set's register contents are valid to use.
  - default access: read only
  - default value: `'No'`
  - possible values: `'No'`, `'Yes'`

`SequencerTriggerActivation` : `enum`  
  Specifies the activation mode of the sequencer trigger.
  - default access: not available
  - possible values: `'RisingEdge'`, `'FallingEdge'`, `'AnyEdge'`, `'LevelHigh'`, `'LevelLow'`

`SequencerTriggerSource` : `enum`  
  Specifies the internal signal or physical input line to use as the sequencer trigger source.
  - default access: read only
  - default value: `'Off'`
  - possible values: `'Off'`, `'FrameStart'`

`SerialPortBaudRate` : `enum`  
  This feature controls the baud rate used by the selected serial port.
  - default access: read/write
  - default value: `'Baud57600'`
  - possible values: `'Baud300'`, `'Baud600'`, `'Baud1200'`, `'Baud2400'`, `'Baud4800'`, `'Baud9600'`, `'Baud14400'`, `'Baud19200'`, `'Baud38400'`, `'Baud57600'`, `'Baud115200'`, `'Baud230400'`, `'Baud460800'`, `'Baud921600'`

`SerialPortBaudRateAddr` : `int`  
  
  - default access: read only
  - default value: `500736`
  - default range: -9223372036854775808 - 9223372036854775807

`SerialPortDataBits` : `int`  
  This feature controls the number of data bits used by the selected serial port.  Possible values that can be used are between 5 and 9.
  - default access: read/write
  - default value: `8`
  - default range: 7 - 8

`SerialPortDataBitsAddr` : `int`  
  
  - default access: read only
  - default value: `501760`
  - default range: -9223372036854775808 - 9223372036854775807

`SerialPortParity` : `enum`  
  This feature controls the parity used by the selected serial port.
  - default access: read/write
  - default value: `'None'`
  - possible values: `'None'`, `'Odd'`, `'Even'`, `'Mark'`, `'Space'`

`SerialPortParityAddr` : `int`  
  
  - default access: read only
  - default value: `503808`
  - default range: -9223372036854775808 - 9223372036854775807

`SerialPortSelector` : `enum`  
  Selects which serial port of the device to control.
  - default access: read/write
  - default value: `'SerialPort0'`
  - possible values: `'SerialPort0'`

`SerialPortSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`SerialPortSource` : `enum`  
  Specifies the physical input Line on which to receive serial data.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'Line0'`, `'Line1'`, `'Line2'`, `'Line3'`, `'Off'`

`SerialPortSourceAddr` : `int`  
  
  - default access: read only
  - default value: `499712`
  - default range: -9223372036854775808 - 9223372036854775807

`SerialPortStopBits` : `enum`  
  This feature controls the number of stop bits used by the selected serial port.
  - default access: read/write
  - default value: `'Bits1'`
  - possible values: `'Bits1'`, `'Bits1AndAHalf'`, `'Bits2'`

`SerialPortStopBitsAddr` : `int`  
  
  - default access: read only
  - default value: `502784`
  - default range: -9223372036854775808 - 9223372036854775807

`SerialReceiveFramingErrorCount` : `int`  
  Returns the number of framing errors that have occurred on the serial port.
  - default access: read only
  - default value: `0`
  - default range: 0 - 4294967295

`SerialReceiveParityErrorCount` : `int`  
  Returns the number of parity errors that have occurred on the serial port.
  - default access: read only
  - default value: `0`
  - default range: 0 - 4294967295

`SerialReceiveQueueCurrentCharacterCount` : `int`  
  Returns the number of characters currently in the serial port receive queue.
  - default access: read only
  - default value: `0`
  - default range: 0 - 4096

`SerialReceiveQueueMaxCharacterCount` : `int`  
  >Returns the maximum number of characters in the serial port receive queue.
  - default access: read only
  - default value: `4096`
  - default range: 0 - 4294967295

`SerialTransmitQueueCurrentCharacterCount` : `int`  
  Returns the number of characters currently in the serial port transmit queue.
  - default access: read only
  - default value: `0`
  - default range: 0 - 4096

`SerialTransmitQueueMaxCharacterCount` : `int`  
  >Returns the maximum number of characters in the serial port transmit queue.
  - default access: read only
  - default value: `4096`
  - default range: 0 - 4294967295

`Sharpening` : `float`  
  Controls the amount to sharpen a signal. The sharpened amount is proportional to the difference between a pixel and its neighbors. A negative value smooths out the difference, while a positive value amplifies the difference. You can boost by a maximum of 8x, but smoothing is limited to 1x  (in float). Default value: 2.0
  - default access: not available
  - default range: -1.0 - 7.999755859375

`SharpeningAuto` : `bool`  
  Enables/disables the auto sharpening feature. When enabled, the camera automatically determines the sharpening threshold based on the noise level of the camera.
  - default access: not available

`SharpeningEnable` : `bool`  
  Enables/disables the sharpening feature. Sharpening is disabled by default.
  - default access: not available

`SharpeningThreshold` : `float`  
  Controls the minimum intensity gradient change to invoke sharpening. When "Sharpening Auto" is enabled, this is determined automatically by the device. The threshold is specified as a fraction of the total intensity range, and ranges from 0 to 0.25. A threshold higher than 25% produces little to no difference than 25%. High thresholds sharpen only areas with significant intensity changes. Low thresholds sharpen more areas.
  - default access: not available
  - default range: 0.0 - 0.2490234375

`TLParamsLocked` : `int`  
  
  - default access: read/write
  - default value: `0`
  - default range: 0 - 1

`Test0001` : `int`  
  For testing only.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4294967295

`TestPattern` : `enum`  
  Selects the type of test pattern that is generated by the device as image source.
  - default access: read/write
  - default value: `'Off'`
  - possible values:
    - `'Off'`: Test pattern is disabled.
    - `'Increment'`: Pixel value increments by 1 for each pixel.
    - `'SensorTestPattern'`: A test pattern generated by the image sensor.  The pattern varies for different sensor models.

`TestPatternAddr` : `int`  
  
  - default access: read only
  - default value: `4026548736`
  - default range: -9223372036854775808 - 9223372036854775807

`TestPatternGeneratorSelector` : `enum`  
  Selects which test pattern generator is controlled by the TestPattern feature.
  - default access: read/write
  - default value: `'Sensor'`
  - possible values:
    - `'Sensor'`: TestPattern feature controls the sensor`s test pattern generator.
    - `'PipelineStart'`: TestPattern feature controls the test pattern inserted at the start of the image pipeline.

`TestPatternGeneratorSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`TestPendingAck` : `int`  
  Test PENDING_ACK feature.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 500

`TimestampIncrement` : `int`  
  Indicates the timestamp increment in ns/tick.
  - default access: read only
  - default value: `1000`
  - default range: 0 - 9223372036854775807

`TimestampLatchValue` : `int`  
  Returns the latched value of the timestamp counter.
  - default access: read only
  - default value: `0`
  - default range: 0 - 9223372036854775807

`TransferBlockCount` : `int`  
  Specifies the number of data blocks (images) that the device should stream before stopping. This feature is only active if the Transfer Operation Mode is set to Multi Block.
  - default access: not available
  - default range: 1 - 1000

`TransferControlMode` : `enum`  
  Selects the control method for the transfers. Basic and Automatic start transmitting data as soon as there is enough data to fill a link layer packet. User Controlled allows you to directly control the transfer of blocks.
  - default access: read/write
  - default value: `'Basic'`
  - possible values:
    - `'Basic'`: Basic
    - `'Automatic'`: Automatic
    - `'UserControlled'`: User Controlled

`TransferOperationMode` : `enum`  
  Selects the operation mode of the transfer. Continuous is similar to Basic/Automatic but you can start/stop the transfer while acquisition runs independently. Multi Block transmits a specified number of blocks and then stops.
  - default access: not available
  - possible values:
    - `'Continuous'`: Continuous
    - `'MultiBlock'`: Multi Block

`TransferQueueCurrentBlockCount` : `int`  
  Returns number of data blocks (images) currently in the transfer queue.
  - default access: read only
  - default value: `0`
  - default range: 0 - 3

`TransferQueueMaxBlockCount` : `int`  
  Returns the maximum number of data blocks (images) in the transfer queue
  - default access: read only
  - default value: `3`
  - default range: 0 - 4294967295

`TransferQueueMode` : `enum`  
  Specifies the operation mode of the transfer queue.
  - default access: not available
  - possible values:
    - `'FirstInFirstOut'`: Blocks first In are transferred Out first.

`TransferQueueOverflowCount` : `int`  
  Returns number of images that have been lost before being transmitted because the transmit queue hasn't been cleared fast enough.
  - default access: read only
  - default value: `0`
  - default range: 0 - 4294967295

`TriggerActivation` : `enum`  
  Specifies the activation mode of the trigger.
  - default access: not available
  - possible values: `'LevelLow'`, `'LevelHigh'`, `'FallingEdge'`, `'RisingEdge'`, `'AnyEdge'`

`TriggerActivationAddr` : `int`  
  
  - default access: read only
  - default value: `823328`
  - default range: -9223372036854775808 - 9223372036854775807

`TriggerDelay` : `float`  
  Specifies the delay in microseconds (??s) to apply after the trigger reception before activating it.
  - default access: read/write
  - default value: `22.0`
  - unit: us
  - default range: 22.0 - 65520.0

`TriggerDelayAddr` : `int`  
  
  - default access: read only
  - default value: `825376`
  - default range: -9223372036854775808 - 9223372036854775807

`TriggerMode` : `enum`  
  Controls whether or not trigger is active.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'Off'`, `'On'`

`TriggerModeAddr` : `int`  
  
  - default access: read only
  - default value: `820256`
  - default range: -9223372036854775808 - 9223372036854775807

`TriggerOverlap` : `enum`  
  Specifies the overlap mode of the trigger.
  - default access: read/write
  - default value: `'Off'`
  - possible values: `'Off'`, `'ReadOut'`, `'PreviousFrame'`

`TriggerOverlapAddr` : `int`  
  
  - default access: read only
  - default value: `824352`
  - default range: -9223372036854775808 - 9223372036854775807

`TriggerSelector` : `enum`  
  Selects the type of trigger to configure.
  - default access: read/write
  - default value: `'FrameStart'`
  - possible values: `'AcquisitionStart'`, `'FrameStart'`, `'FrameBurstStart'`

`TriggerSelectorValueToIndex` : `int`  
  
  - default access: read only
  - default value: `1`
  - default range: -9223372036854775808 - 9223372036854775807

`TriggerSoftwareAddr` : `int`  
  
  - default access: read only
  - default value: `821280`
  - default range: -9223372036854775808 - 9223372036854775807

`TriggerSource` : `enum`  
  Specifies the internal signal or physical input line to use as the trigger source.
  - default access: read/write
  - default value: `'Software'`
  - possible values: `'Software'`, `'Line0'`, `'Line1'`, `'Line2'`, `'Line3'`, `'UserOutput0'`, `'UserOutput1'`, `'UserOutput2'`, `'UserOutput3'`, `'Counter0Start'`, `'Counter1Start'`, `'Counter0End'`, `'Counter1End'`, `'LogicBlock0'`, `'LogicBlock1'`, `'Action0'`

`TriggerSourceAddr` : `int`  
  
  - default access: read only
  - default value: `822304`
  - default range: -9223372036854775808 - 9223372036854775807

`U3VAccessPrivilege` : `int`  
  Access Privilege.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4294967295

`U3VCPCapability` : `int`  
  Indicates additional features on the control channel.
  - default access: read only
  - default value: `0`
  - default range: -9223372036854775808 - 9223372036854775807

`U3VCPEIRMAvailable` : `bool`  
  Set if the device supports at least one device event interface.
  - default access: read only
  - default value: `True`

`U3VCPIIDC2Available` : `bool`  
  Set if the device supports IIDC2 register map.
  - default access: read only
  - default value: `False`

`U3VCPSIRMAvailable` : `bool`  
  Set if the device supports at least one device streaming interface.
  - default access: read only
  - default value: `True`

`U3VCurrentSpeed` : `enum`  
  Specifies the current speed of the USB link.
  - default access: read only
  - default value: `'SuperSpeed'`
  - possible values: `'LowSpeed'`, `'FullSpeed'`, `'HighSpeed'`, `'SuperSpeed'`

`U3VMaxAcknowledgeTransferLength` : `int`  
  Specifies the max suuported ack transfer length of the device.
  - default access: read only
  - default value: `1024`
  - default range: 0 - 4294967295

`U3VMaxCommandTransferLength` : `int`  
  Specifies the max suuported command transfer length of the device.
  - default access: read only
  - default value: `1024`
  - default range: 0 - 4294967295

`U3VMaxDeviceResponseTime` : `int`  
  Max Resonse Time in ms.
  - default access: read only
  - default value: `200`
  - default range: 0 - 4294967295

`U3VMessageChannelID` : `int`  
  Channel ID Used For The Message Channel.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 4294967295

`U3VNumberOfStreamChannels` : `int`  
  Number of Stream Channels and its Corresponding Streaming Interface Register Maps.
  - default access: read only
  - default value: `1`
  - default range: 0 - 4294967295

`U3VVersionMajor` : `int`  
  U3V Version.
  - default access: read only
  - default value: `1`
  - default range: 0 - 65535

`U3VVersionMinor` : `int`  
  U3V Version.
  - default access: read only
  - default value: `0`
  - default range: 0 - 65535

`UserOutputSelector` : `enum`  
  Selects which bit of the User Output register is set by UserOutputValue.
  - default access: read/write
  - default value: `'UserOutput0'`
  - possible values: `'UserOutput0'`, `'UserOutput1'`, `'UserOutput2'`, `'UserOutput3'`

`UserOutputValue` : `bool`  
  Value of the selected user output, either logic high (enabled) or logic low (disabled).
  - default access: read/write
  - default value: `False`

`UserOutputValueAll` : `int`  
  Returns the current status of all the user output status bits in a hexadecimal representation (UserOutput 0 status corresponds to bit 0, UserOutput 1 status with bit 1, etc). This allows simultaneous reading of all user output statuses at once.
  - default access: read/write
  - default value: `0`
  - default range: 0 - 15

`UserSetDefault` : `enum`  
  Selects the feature User Set to load and make active by default when the device is restarted.
  - default access: read/write
  - default value: `'Default'`
  - possible values:
    - `'Default'`: Factory default set.
    - `'UserSet0'`: User configurable set 0.
    - `'UserSet1'`: User configurable set 1.

`UserSetFeatureEnable` : `bool`  
  Whether or not the selected feature is saved to user sets.
  - default access: read only
  - default value: `True`

`UserSetFeatureSelector` : `enum`  
  List of features that are saved to user sets.
  - default access: read/write
  - default value: `'AasRoiEnableAe'`
  - possible values: `'AasRoiEnableAe'`, `'AasRoiEnableAwb'`, `'AasRoiHeightAe'`, `'AasRoiHeightAwb'`, `'AasRoiOffsetXAe'`, `'AasRoiOffsetXAwb'`, `'AasRoiOffsetYAe'`, `'AasRoiOffsetYAwb'`, `'AasRoiWidthAe'`, `'AasRoiWidthAwb'`, `'AcquisitionBurstFrameCount'`, `'AcquisitionFrameCount'`, `'AcquisitionFrameRate'`, `'AcquisitionFrameRateEnable'`, `'AcquisitionLineRate'`, `'AcquisitionMode'`, `'AdcBitDepth'`, `'AutoExposureControlLoopDamping'`, `'AutoExposureControlPriority'`, `'AutoExposureEVCompensation'`, `'AutoExposureExposureTimeLowerLimit'`, `'AutoExposureExposureTimeUpperLimit'`, `'AutoExposureGainLowerLimit'`, `'AutoExposureGainUpperLimit'`, `'AutoExposureGreyValueLowerLimit'`, `'AutoExposureGreyValueUpperLimit'`, `'AutoExposureLightingMode'`, `'AutoExposureMeteringMode'`, `'AutoExposureTargetGreyValue'`, `'AutoExposureTargetGreyValueAuto'`, `'BalanceRatioBlue'`, `'BalanceRatioRed'`, `'BalanceWhiteAuto'`, `'BalanceWhiteAutoDamping'`, `'BalanceWhiteAutoLowerLimit'`, `'BalanceWhiteAutoProfile'`, `'BalanceWhiteAutoUpperLimit'`, `'BinningHorizontalAll'`, `'BinningHorizontalMode'`, `'BinningVerticalAll'`, `'BinningVerticalMode'`, `'BlackLevelAll'`, `'ChunkEnableAll'`, `'ChunkModeActive'`, `'ColorTransformationEnable'`, `'CounterDelayCounter0'`, `'CounterDelayCounter1'`, `'CounterDurationCounter0'`, `'CounterDurationCounter1'`, `'CounterEventActivationCounter0'`, `'CounterEventActivationCounter1'`, `'CounterEventSourceCounter0'`, `'CounterEventSourceCounter1'`, `'CounterResetActivationCounter0'`, `'CounterResetActivationCounter1'`, `'CounterResetSourceCounter0'`, `'CounterResetSourceCounter1'`, `'CounterTriggerActivationCounter0'`, `'CounterTriggerActivationCounter1'`, `'CounterTriggerSourceCounter0'`, `'CounterTriggerSourceCounter1'`, `'DecimationHorizontalAll'`, `'DecimationVerticalAll'`, `'DefectCorrectStaticEnable'`, `'DefectCorrectionMode'`, `'DeviceIndicatorMode'`, `'DeviceLinkBandwidthReserve'`, `'DeviceLinkThroughputLimit'`, `'EvCompensationRaw'`, `'EventNotificationError'`, `'EventNotificationExposureEnd'`, `'EventNotificationSerialPortReceive'`, `'ExposureActiveMode'`, `'ExposureAuto'`, `'ExposureMode'`, `'ExposureTime'`, `'FfcEnable'`, `'FfcMode'`, `'GainAll'`, `'GainAuto'`, `'Gamma'`, `'GammaEnable'`, `'Height'`, `'IspEnable'`, `'LUTEnable'`, `'LineFilterWidthLine0Debounce'`, `'LineFilterWidthLine0Deglitch'`, `'LineFilterWidthLine1Debounce'`, `'LineFilterWidthLine1Deglitch'`, `'LineFilterWidthLine2Debounce'`, `'LineFilterWidthLine2Deglitch'`, `'LineFilterWidthLine3Debounce'`, `'LineFilterWidthLine3Deglitch'`, `'LineInverterLine0'`, `'LineInverterLine1'`, `'LineInverterLine2'`, `'LineInverterLine3'`, `'LineModeLine0'`, `'LineModeLine1'`, `'LineModeLine2'`, `'LineModeLine3'`, `'LineSourceLine0'`, `'LineSourceLine1'`, `'LineSourceLine2'`, `'LineSourceLine3'`, `'LogicBlockLUTInputActivationLogicBlock0Input0'`, `'LogicBlockLUTInputActivationLogicBlock0Input1'`, `'LogicBlockLUTInputActivationLogicBlock0Input2'`, `'LogicBlockLUTInputActivationLogicBlock0Input3'`, `'LogicBlockLUTInputActivationLogicBlock1Input0'`, `'LogicBlockLUTInputActivationLogicBlock1Input1'`, `'LogicBlockLUTInputActivationLogicBlock1Input2'`, `'LogicBlockLUTInputActivationLogicBlock1Input3'`, `'LogicBlockLUTInputSourceLogicBlock0Input0'`, `'LogicBlockLUTInputSourceLogicBlock0Input1'`, `'LogicBlockLUTInputSourceLogicBlock0Input2'`, `'LogicBlockLUTInputSourceLogicBlock0Input3'`, `'LogicBlockLUTInputSourceLogicBlock1Input0'`, `'LogicBlockLUTInputSourceLogicBlock1Input1'`, `'LogicBlockLUTInputSourceLogicBlock1Input2'`, `'LogicBlockLUTInputSourceLogicBlock1Input3'`, `'LogicBlockLUTOutputValueAllLogicBlock0Enable'`, `'LogicBlockLUTOutputValueAllLogicBlock0Value'`, `'LogicBlockLUTOutputValueAllLogicBlock1Enable'`, `'LogicBlockLUTOutputValueAllLogicBlock1Value'`, `'OffsetX'`, `'OffsetY'`, `'PixelFormat'`, `'ReverseX'`, `'ReverseY'`, `'RgbTransformLightSource'`, `'Saturation'`, `'SaturationEnable'`, `'SensorShutterMode'`, `'SerialPortBaudRateSerialPort0'`, `'SerialPortDataBitsSerialPort0'`, `'SerialPortParitySerialPort0'`, `'SerialPortSourceSerialPort0'`, `'SerialPortStopBitsSerialPort0'`, `'Sharpening'`, `'SharpeningAuto'`, `'SharpeningEnable'`, `'SharpeningThreshold'`, `'TestPatternPipelineStart'`, `'TestPatternSensor'`, `'TransferBlockCount'`, `'TransferControlMode'`, `'TransferOperationMode'`, `'TriggerActivationAcquisitionStart'`, `'TriggerActivationFrameBurstStart'`, `'TriggerActivationFrameStart'`, `'TriggerDelayAcquisitionStart'`, `'TriggerDelayFrameBurstStart'`, `'TriggerDelayFrameStart'`, `'TriggerModeAcquisitionStart'`, `'TriggerModeFrameBurstStart'`, `'TriggerModeFrameStart'`, `'TriggerOverlapAcquisitionStart'`, `'TriggerOverlapFrameBurstStart'`, `'TriggerOverlapFrameStart'`, `'TriggerSourceAcquisitionStart'`, `'TriggerSourceFrameBurstStart'`, `'TriggerSourceFrameStart'`, `'UserOutputValueAll'`, `'3EnableLine0'`, `'3EnableLine1'`, `'3EnableLine2'`, `'3EnableLine3'`, `'Width'`

`UserSetSelector` : `enum`  
  Selects the feature User Set to load, save or configure.
  - default access: read/write
  - default value: `'Default'`
  - possible values:
    - `'Default'`: Factory default set.
    - `'UserSet0'`: User configurable set 0.
    - `'UserSet1'`: User configurable set 1.

`VbinAddr` : `int`  
  
  - default access: read only
  - default value: `541696`
  - default range: -9223372036854775808 - 9223372036854775807

`VdecAddr` : `int`  
  
  - default access: read only
  - default value: `542720`
  - default range: -9223372036854775808 - 9223372036854775807

`Width` : `int`  
  Width of the image provided by the device (in pixels).
  - default access: read/write
  - default value: `4096`
  - default range: 8 - 4096

`WidthMax` : `int`  
  Maximum width of the image (in pixels). The dimension is calculated after horizontal binning. WidthMax does not take into account the current Region of interest (Width or OffsetX).
  - default access: read only
  - default value: `4096`
  - default range: 0 - 4294967295

Commands
--------

**Note: the camera recording should be started/stopped using the `start` and `stop` methods, not any of the functions below (see simple_pyspin documentation).**

`AcquisitionStart()`:  
  This command starts the acquisition of images.
  - default access: not available

`AcquisitionStop()`:  
  This command stops the acquisition of images.
  - default access: write only

`DefectTableApply()`:  
  Applies the current defect table, so that any changes made affect images captured by the camera. This writes the table to volatile memory, so changes to the table are lost if the camera loses power. To save the table to non-volatile memory, use DefectTableSave.
  - default access: read/write

`DefectTableFactoryRestore()`:  
  Restores the Defective Pixel Table to its factory default state, which was calibrated during manufacturing. This permanently overwrites any changes made to the defect table.
  - default access: read/write

`DefectTableSave()`:  
  Saves the current defective pixel table non-volatile memory, so that it is preserved when the camera boots up. This overwrites the existing defective pixel table. The new table is loaded whenever the camera powers up.
  - default access: write only

`DeviceReset()`:  
  This is a command that immediately resets and reboots the device.
  - default access: write only

`FactoryReset()`:  
  Returns all user tables to factory default
  - default access: write only

`FfcUserTableReset()`:  
  Resets the user flat field correction table to the last saved values loaded from the camera. If nothing has been previously saved, this resets to the default values which is the equivalent of disabling FFC.
  - default access: not available

`FfcUserTableSave()`:  
  Saves the current User flat field correction table into the camera, which means the table is still available after a power cycle. Note that this overwrites the existing saved User table.
  - default access: not available

`FileOperationExecute()`:  
  This is a command that executes the selected file operation on the selected file.
  - default access: write only

`SequencerConfigurationReset()`:  
  Resets the sequencer configuration by erasing all saved sequencer sets.
  - default access: read only

`SequencerSetLoad()`:  
  Loads currently selected sequencer to the current device configuration.
  - default access: read only

`SequencerSetSave()`:  
  Saves the current device configuration to the currently selected sequencer set.
  - default access: read only

`SerialReceiveQueueClear()`:  
  This is a command that clears the device serial port receive queue.
  - default access: write only

`TestEventGenerate()`:  
  This command generates a test event and sends it to the host.
  - default access: write only

`TimestampLatch()`:  
  Latches the current timestamp counter into TimestampLatchValue.
  - default access: write only

`TransferStart()`:  
  Starts the streaming of data blocks (images) out of the device. This feature is available when the Transfer Control Mode is set to User Controlled.
  - default access: not available

`TransferStop()`:  
  Stops the streaming of data block (images). The current block transmission is completed. This feature is available when the Transfer Control Mode is set to User Controlled.
  - default access: not available

`TriggerEventTest()`:  
  This command generates a test event and sends it to the host.
  - default access: write only

`TriggerSoftware()`:  
  Generates an internal trigger if Trigger Source is set to Software.
  - default access: not available

`UserSetLoad()`:  
  Loads the User Set specified by UserSetSelector to the device and makes it active.
  - default access: read/write

`UserSetSave()`:  
  Saves the User Set specified by UserSetSelector to the non-volatile memory of the device.
  - default access: read only
