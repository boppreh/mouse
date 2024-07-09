
mouse
=====

Take full control of your mouse with this small Python library. Hook global events, register hotkeys, simulate mouse movement and clicks, and much more.

_Huge thanks to [Kirill Pavlov](http://kirillpavlov.com/) for donating the package name. If you are looking for the Cheddargetter.com client implementation, [`pip install mouse==0.5.0`](https://pypi.python.org/pypi/mouse/0.5.0)._

## Features

- Global event hook on all mice devices (captures events regardless of focus).
- **Listen** and **sends** mouse events.
- Works with **Windows** and **Linux** (requires sudo).
- Works with **macOS** (requires granting accessibility permissions to terminal/python in System Preferences -> Security \& Privacy)
- **Pure Python**, no C modules to be compiled.
- **Zero dependencies** on Windows and Linux. Trivial to install and deploy, just copy the files.
- **Python 2 and 3**.
- Includes **high level API** (e.g. [record](#mouse.record) and [play](#mouse.play)).
- Events automatically captured in separate thread, doesn't block main program.
- Tested and documented.

This program makes no attempt to hide itself, so don't use it for keyloggers.

## Usage

Install the [PyPI package](https://pypi.python.org/pypi/mouse/):

    $ sudo pip install mouse

or clone the repository (no installation required, source files are sufficient):

    $ git clone https://github.com/boppreh/mouse

Then check the [API docs](https://github.com/boppreh/mouse#api) to see what features are available.


## Known limitations:

- Events generated under Windows don't report device id (`event.device == None`). [#21](https://github.com/boppreh/keyboard/issues/21)
- To avoid depending on X the Linux parts reads raw device files (`/dev/input/input*`) but this requires root.
- Other applications, such as some games, may register hooks that swallow all key events. In this case `mouse` will be unable to report events.



# API
#### Table of Contents

- [class mouse.**ButtonEvent**](#class-mousebuttonevent)
  * [ButtonEvent.**button**](#buttoneventbutton)
  * [ButtonEvent.**count**(self, value, /)](#buttoneventcountself-value-)
  * [ButtonEvent.**event\_type**](#buttoneventevent_type)
  * [ButtonEvent.**index**(self, value, start=0, stop=9223372036854775807, /)](#buttoneventindexself-value-start0-stop9223372036854775807-)
  * [ButtonEvent.**time**](#buttoneventtime)
- [mouse.**DOUBLE**](#mousedouble)
- [mouse.**DOWN**](#mousedown)
- [mouse.**LEFT**](#mouseleft)
- [mouse.**MIDDLE**](#mousemiddle)
- [class mouse.**MoveEvent**](#class-mousemoveevent)
  * [MoveEvent.**count**(self, value, /)](#moveeventcountself-value-)
  * [MoveEvent.**index**(self, value, start=0, stop=9223372036854775807, /)](#moveeventindexself-value-start0-stop9223372036854775807-)
  * [MoveEvent.**time**](#moveeventtime)
  * [MoveEvent.**x**](#moveeventx)
  * [MoveEvent.**y**](#moveeventy)
- [mouse.**RIGHT**](#mouseright)
- [mouse.**UP**](#mouseup)
- [class mouse.**WheelEvent**](#class-mousewheelevent)
  * [WheelEvent.**count**(self, value, /)](#wheeleventcountself-value-)
  * [WheelEvent.**delta**](#wheeleventdelta)
  * [WheelEvent.**index**(self, value, start=0, stop=9223372036854775807, /)](#wheeleventindexself-value-start0-stop9223372036854775807-)
  * [WheelEvent.**time**](#wheeleventtime)
- [mouse.**X**](#mousex)
- [mouse.**X2**](#mousex2)
- [mouse.**version**](#mouseversion)
- [mouse.**is\_pressed**(button=&#x27;left&#x27;)](#mouseis_pressedbuttonleft)
- [mouse.**press**(button=&#x27;left&#x27;)](#mousepressbuttonleft)
- [mouse.**release**(button=&#x27;left&#x27;)](#mousereleasebuttonleft)
- [mouse.**click**(button=&#x27;left&#x27;)](#mouseclickbuttonleft)
- [mouse.**double\_click**(button=&#x27;left&#x27;)](#mousedouble_clickbuttonleft)
- [mouse.**scroll\_wheel**(delta=1)](#mousescroll_wheeldelta1)
- [mouse.**move**(x, y, absolute=True, duration=0, steps_per_second=120.0)](#mousemovex-y-absolutetrue-duration0-steps_per_second1200)
- [mouse.**drag**(start\_x, start\_y, end\_x, end\_y, button=&#x27;left&#x27; absolute=True, move_duration=0, drag_duration=0)](#mousedragstart_x-start_y-end_x-end_y-buttonleft-absolutetrue-move_duration0-drag_duration0)
- [mouse.**on\_move**(callback, args=())](#mouseon_movecallback-args)
- [mouse.**on\_button**(callback, args=(), buttons=(&#x27;left&#x27;, &#x27;middle&#x27;, &#x27;right&#x27;, &#x27;x&#x27;, &#x27;x2&#x27;), types=(&#x27;up&#x27;, &#x27;down&#x27;, &#x27;double&#x27;))](#mouseon_buttoncallback-args-buttonsleft-middle-right-x-x2-typesup-down-double)
- [mouse.**on\_press**(callback, args=(), button=&#x27;left&#x27;)](#mouseon_presscallback-args-buttonleft)
- [mouse.**on\_release**(callback, args=(), button=&#x27;left&#x27;)](#mouseon_releasecallback-args-buttonleft)
- [mouse.**on\_double\_click**(callback, args=(), button=&#x27;left&#x27;)](#mouseon_double_clickcallback-args-buttonleft)
- [mouse.**wait**(button=None, target\_types=(&#x27;up&#x27;, &#x27;down&#x27;, &#x27;double&#x27;))](#mousewaitbuttonnone-target_typesup-down-double)
- [mouse.**get\_position**()](#mouseget_position)
- [mouse.**hook**(callback)](#mousehookcallback)
- [mouse.**unhook**(callback)](#mouseunhookcallback)
- [mouse.**unhook\_all**()](#mouseunhook_all)
- [mouse.**record**(button=&#x27;right&#x27;, target\_types=(&#x27;down&#x27;,))](#mouserecordbuttonright-target_typesdown)
- [mouse.**play**(events, speed\_factor=1.0, include\_clicks=True, include\_moves=True, include\_wheel=True)](#mouseplayevents-speed_factor10-include_clickstrue-include_movestrue-include_wheeltrue)


<a name="mouse.ButtonEvent"></a>

## class mouse.**ButtonEvent**

ButtonEvent(event_type, button, time)


<a name="ButtonEvent.button"></a>

### ButtonEvent.**button**

Alias for field number 1


<a name="ButtonEvent.count"></a>

### ButtonEvent.**count**(self, value, /)

Return number of occurrences of value.


<a name="ButtonEvent.event_type"></a>

### ButtonEvent.**event\_type**

Alias for field number 0


<a name="ButtonEvent.index"></a>

### ButtonEvent.**index**(self, value, start=0, stop=9223372036854775807, /)

Return first index of value.

Raises ValueError if the value is not present.


<a name="ButtonEvent.time"></a>

### ButtonEvent.**time**

Alias for field number 2


<a name="mouse.DOUBLE"></a>

## mouse.**DOUBLE**
```py
= 'double'
```

<a name="mouse.DOWN"></a>

## mouse.**DOWN**
```py
= 'down'
```

<a name="mouse.LEFT"></a>

## mouse.**LEFT**
```py
= 'left'
```

<a name="mouse.MIDDLE"></a>

## mouse.**MIDDLE**
```py
= 'middle'
```

<a name="mouse.MoveEvent"></a>

## class mouse.**MoveEvent**

MoveEvent(x, y, time)


<a name="MoveEvent.count"></a>

### MoveEvent.**count**(self, value, /)

Return number of occurrences of value.


<a name="MoveEvent.index"></a>

### MoveEvent.**index**(self, value, start=0, stop=9223372036854775807, /)

Return first index of value.

Raises ValueError if the value is not present.


<a name="MoveEvent.time"></a>

### MoveEvent.**time**

Alias for field number 2


<a name="MoveEvent.x"></a>

### MoveEvent.**x**

Alias for field number 0


<a name="MoveEvent.y"></a>

### MoveEvent.**y**

Alias for field number 1


<a name="mouse.RIGHT"></a>

## mouse.**RIGHT**
```py
= 'right'
```

<a name="mouse.UP"></a>

## mouse.**UP**
```py
= 'up'
```

<a name="mouse.WheelEvent"></a>

## class mouse.**WheelEvent**

WheelEvent(delta, time)


<a name="WheelEvent.count"></a>

### WheelEvent.**count**(self, value, /)

Return number of occurrences of value.


<a name="WheelEvent.delta"></a>

### WheelEvent.**delta**

Alias for field number 0


<a name="WheelEvent.index"></a>

### WheelEvent.**index**(self, value, start=0, stop=9223372036854775807, /)

Return first index of value.

Raises ValueError if the value is not present.


<a name="WheelEvent.time"></a>

### WheelEvent.**time**

Alias for field number 1


<a name="mouse.X"></a>

## mouse.**X**
```py
= 'x'
```

<a name="mouse.X2"></a>

## mouse.**X2**
```py
= 'x2'
```

<a name="mouse.version"></a>

## mouse.**version**
```py
= '0.7.2'
```

<a name="mouse.is_pressed"></a>

## mouse.**is\_pressed**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L86)

Returns True if the given button is currently pressed.


<a name="mouse.press"></a>

## mouse.**press**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L92)

Presses the given button (but doesn't release).


<a name="mouse.release"></a>

## mouse.**release**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L97)

Releases the given button.


<a name="mouse.click"></a>

## mouse.**click**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L102)

Sends a click with the given button.


<a name="mouse.double_click"></a>

## mouse.**double\_click**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L108)

Sends a double click with the given button.


<a name="mouse.scroll_wheel"></a>

## mouse.**scroll\_wheel**(delta=1)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L114)

Scrolls the wheel by `delta` clicks. Sign indicates direction.


<a name="mouse.move"></a>

## mouse.**move**(x, y, absolute=True, duration=0, steps_per_second=120.0)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L119)


Moves the mouse. If `absolute`, to position (x, y), otherwise move relative
to the current position. If `duration` is non-zero, animates the movement.
The steps_per_second is only an approximation. Due to the internal sleep's
unreliability it cannot be followed strictly. The less its value is, the more
valid the number becomes.

<a name="mouse.drag"></a>

## mouse.**drag**(start\_x, start\_y, end\_x, end\_y, button=&#x27;left&#x27; absolute=True, move_duration=0, drag_duration=0)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L176)


Holds the specified mouse button, moving from start to end position, then
releases. `absolute`, `move_duration` are parameters regarding the mouse movement.
`drag_duration` is a parameter regarding the drag speed.


<a name="mouse.on_move"></a>

## mouse.**on\_move**(callback, args=())

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L190)

Invokes `callback` with `args` when the mouse moves.


<a name="mouse.on_button"></a>

## mouse.**on\_button**(callback, args=(), buttons=(&#x27;left&#x27;, &#x27;middle&#x27;, &#x27;right&#x27;, &#x27;x&#x27;, &#x27;x2&#x27;), types=(&#x27;up&#x27;, &#x27;down&#x27;, &#x27;double&#x27;))

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L200)

Invokes `callback` with `args` when the specified event happens.


<a name="mouse.on_press"></a>

## mouse.**on\_press**(callback, args=(), button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L216)

Invokes `callback` with `args` when the specified button is pressed.


<a name="mouse.on_click"></a>

## mouse.**on\_release**(callback, args=(), button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L221)

Invokes `callback` with `args` when the specified button is released/clicked.


<a name="mouse.on_double_click"></a>

## mouse.**on\_double\_click**(callback, args=(), button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L226)

Invokes `callback` with `args` when the specified button is double-clicked.


<a name="mouse.wait"></a>

## mouse.**wait**(button=None, target\_types=(&#x27;up&#x27;, &#x27;down&#x27;, &#x27;double&#x27;))

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L233)

Blocks program execution until the given button performs an event or, if given no parameters, blocks forever.


<a name="mouse.get_position"></a>

## mouse.**get\_position**()

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L250)

Returns the (x, y) mouse position.


<a name="mouse.hook"></a>

## mouse.**hook**(callback)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L255)


Installs a global listener on all available mouses, invoking `callback`
each time it is moved, a key status changes or the wheel is spun. A mouse
event is passed as argument, with type either `mouse.ButtonEvent`,
`mouse.WheelEvent` or `mouse.MoveEvent`.

Returns the given callback for easier development.


<a name="mouse.unhook"></a>

## mouse.**unhook**(callback)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L268)


Removes a previously installed hook.


<a name="mouse.unhook_all"></a>

## mouse.**unhook\_all**()

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L275)


Removes all hooks registered by this application. Note this may include
hooks installed by high level functions, such as [`record`](#mouse.record).


<a name="mouse.record"></a>

## mouse.**record**(button=&#x27;right&#x27;, target\_types=(&#x27;down&#x27;,))

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L283)


Records all mouse events until the user presses the given button.
Then returns the list of events recorded. Pairs well with [`play(events)`](#mouse.play).

Note: this is a blocking function.
Note: for more details on the mouse hook and events see [`hook`](#mouse.hook).


<a name="mouse.play"></a>

## mouse.**play**(events, speed\_factor=1.0, include\_clicks=True, include\_moves=True, include\_wheel=True)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L298)


Plays a sequence of recorded events, maintaining the relative time
intervals. If speed_factor is <= 0 then the actions are replayed as fast
as the OS allows. Pairs well with [`record()`](#mouse.record).

The parameters `include_*` define if events of that type should be included
in the replay or ignored.
