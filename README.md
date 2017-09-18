
mouse
=====

Take full control of your mouse with this small Python library. Hook global events, register hotkeys, simulate mouse movement and clicks, and much more.

_Huge thanks to [Kirill Pavlov](http://kirillpavlov.com/) for donating the package name. If you are looking for the Cheddargetter.com client implementation, [`pip install mouse==0.5.0`](https://pypi.python.org/pypi/mouse/0.5.0)._

## Features

- Global event hook on all mice devices (captures events regardless of focus).
- **Listen** and **sends** mouse events.
- Works with **Windows** and **Linux** (requires sudo).
- **Pure Python**, no C modules to be compiled.
- **Zero dependencies**. Trivial to install and deploy, just copy the files.
- **Python 2 and 3**.
- Includes **high level API** (e.g. [record](#mouse.record) and [play](#mouse.play).
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
- To avoid depending on X the Linux parts reads raw device files (`/dev/input/input*`) but this requries root.
- Other applications, such as some games, may register hooks that swallow all key events. In this case `mouse` will be unable to report events.



# API
#### Table of Contents

- [mouse.**ButtonEvent**](#mouse.ButtonEvent)
- [mouse.**DOUBLE**](#mouse.DOUBLE)
- [mouse.**DOWN**](#mouse.DOWN)
- [mouse.**LEFT**](#mouse.LEFT)
- [mouse.**MIDDLE**](#mouse.MIDDLE)
- [mouse.**MoveEvent**](#mouse.MoveEvent)
- [mouse.**RIGHT**](#mouse.RIGHT)
- [mouse.**UP**](#mouse.UP)
- [mouse.**WheelEvent**](#mouse.WheelEvent)
- [mouse.**X**](#mouse.X)
- [mouse.**X2**](#mouse.X2)
- [mouse.**is\_pressed**](#mouse.is_pressed)
- [mouse.**press**](#mouse.press)
- [mouse.**hold**](#mouse.hold) *(alias)*
- [mouse.**release**](#mouse.release)
- [mouse.**click**](#mouse.click)
- [mouse.**double\_click**](#mouse.double_click)
- [mouse.**right\_click**](#mouse.right_click)
- [mouse.**wheel**](#mouse.wheel)
- [mouse.**move**](#mouse.move)
- [mouse.**drag**](#mouse.drag)
- [mouse.**on\_button**](#mouse.on_button)
- [mouse.**on\_click**](#mouse.on_click)
- [mouse.**on\_double\_click**](#mouse.on_double_click)
- [mouse.**on\_right\_click**](#mouse.on_right_click)
- [mouse.**on\_middle\_click**](#mouse.on_middle_click)
- [mouse.**wait**](#mouse.wait)
- [mouse.**get\_position**](#mouse.get_position)
- [mouse.**hook**](#mouse.hook)
- [mouse.**unhook**](#mouse.unhook)
- [mouse.**unhook\_all**](#mouse.unhook_all)
- [mouse.**record**](#mouse.record)
- [mouse.**play**](#mouse.play)
- [mouse.**replay**](#mouse.replay) *(alias)*


<a name="mouse.ButtonEvent"/>

## class mouse.**ButtonEvent**

ButtonEvent(event_type, button, time)


<a name="ButtonEvent.button"/>

### ButtonEvent.**button**

Alias for field number 1


<a name="ButtonEvent.count"/>

### ButtonEvent.**count**(...)

T.count(value) -> integer -- return number of occurrences of value


<a name="ButtonEvent.event_type"/>

### ButtonEvent.**event\_type**

Alias for field number 0


<a name="ButtonEvent.index"/>

### ButtonEvent.**index**(...)

T.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.


<a name="ButtonEvent.time"/>

### ButtonEvent.**time**

Alias for field number 2




<a name="mouse.DOUBLE"/>

## mouse.**DOUBLE**
    = 'double'


<a name="mouse.DOWN"/>

## mouse.**DOWN**
    = 'down'


<a name="mouse.LEFT"/>

## mouse.**LEFT**
    = 'left'


<a name="mouse.MIDDLE"/>

## mouse.**MIDDLE**
    = 'middle'


<a name="mouse.MoveEvent"/>

## class mouse.**MoveEvent**

MoveEvent(x, y, time)


<a name="MoveEvent.count"/>

### MoveEvent.**count**(...)

T.count(value) -> integer -- return number of occurrences of value


<a name="MoveEvent.index"/>

### MoveEvent.**index**(...)

T.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.


<a name="MoveEvent.time"/>

### MoveEvent.**time**

Alias for field number 2


<a name="MoveEvent.x"/>

### MoveEvent.**x**

Alias for field number 0


<a name="MoveEvent.y"/>

### MoveEvent.**y**

Alias for field number 1




<a name="mouse.RIGHT"/>

## mouse.**RIGHT**
    = 'right'


<a name="mouse.UP"/>

## mouse.**UP**
    = 'up'


<a name="mouse.WheelEvent"/>

## class mouse.**WheelEvent**

WheelEvent(delta, time)


<a name="WheelEvent.count"/>

### WheelEvent.**count**(...)

T.count(value) -> integer -- return number of occurrences of value


<a name="WheelEvent.delta"/>

### WheelEvent.**delta**

Alias for field number 0


<a name="WheelEvent.index"/>

### WheelEvent.**index**(...)

T.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.


<a name="WheelEvent.time"/>

### WheelEvent.**time**

Alias for field number 1




<a name="mouse.X"/>

## mouse.**X**
    = 'x'


<a name="mouse.X2"/>

## mouse.**X2**
    = 'x2'


<a name="mouse.is_pressed"/>

## mouse.**is\_pressed**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L73)

Returns True if the given button is currently pressed. 


<a name="mouse.press"/>

## mouse.**press**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L78)

Presses the given button (but doesn't release). 


<a name="mouse.hold"/>

## mouse.**hold**

Alias for [`press`](#mouse.press).


<a name="mouse.release"/>

## mouse.**release**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L82)

Releases the given button. 


<a name="mouse.click"/>

## mouse.**click**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L86)

Sends a click with the given button. 


<a name="mouse.double_click"/>

## mouse.**double\_click**(button=&#x27;left&#x27;)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L91)

Sends a double click with the given button. 


<a name="mouse.right_click"/>

## mouse.**right\_click**()

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L96)

Sends a right click with the given button. 


<a name="mouse.wheel"/>

## mouse.**wheel**(delta=1)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L100)

Scrolls the wheel `delta` clicks. Sign indicates direction. 


<a name="mouse.move"/>

## mouse.**move**(x, y, absolute=True, duration=0)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L104)


Moves the mouse. If `absolute`, to position (x, y), otherwise move relative
to the current position. If `duration` is non-zero, animates the movement.



<a name="mouse.drag"/>

## mouse.**drag**(start\_x, start\_y, end\_x, end\_y, absolute=True, duration=0)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L138)


Holds the left mouse button, moving from start to end position, then
releases. `absolute` and `duration` are parameters regarding the mouse
movement.



<a name="mouse.on_button"/>

## mouse.**on\_button**(callback, args=(), buttons=(&#x27;left&#x27;, &#x27;middle&#x27;, &#x27;right&#x27;, &#x27;x&#x27;, &#x27;x2&#x27;), types=(&#x27;up&#x27;, &#x27;down&#x27;, &#x27;double&#x27;))

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L151)

Invokes `callback` with `args` when the specified event happens. 


<a name="mouse.on_click"/>

## mouse.**on\_click**(callback, args=())

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L165)

Invokes `callback` with `args` when the left button is clicked. 


<a name="mouse.on_double_click"/>

## mouse.**on\_double\_click**(callback, args=())

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L169)


Invokes `callback` with `args` when the left button is double clicked.



<a name="mouse.on_right_click"/>

## mouse.**on\_right\_click**(callback, args=())

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L175)

Invokes `callback` with `args` when the right button is clicked. 


<a name="mouse.on_middle_click"/>

## mouse.**on\_middle\_click**(callback, args=())

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L179)

Invokes `callback` with `args` when the middle button is clicked. 


<a name="mouse.wait"/>

## mouse.**wait**(button=&#x27;left&#x27;, target\_types=(&#x27;up&#x27;, &#x27;down&#x27;, &#x27;double&#x27;))

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L183)


Blocks program execution until the given button performs an event.



<a name="mouse.get_position"/>

## mouse.**get\_position**()

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L194)

Returns the (x, y) mouse position. 


<a name="mouse.hook"/>

## mouse.**hook**(callback)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L198)


Installs a global listener on all available mouses, invoking `callback`
each time it is moved, a key status changes or the wheel is spun. A mouse
event is passed as argument, with type either `mouse.ButtonEvent`,
`mouse.WheelEvent` or `mouse.MoveEvent`.

Returns the given callback for easier development.



<a name="mouse.unhook"/>

## mouse.**unhook**(callback)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L210)


Removes a previously installed hook.



<a name="mouse.unhook_all"/>

## mouse.**unhook\_all**()

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L216)


Removes all hooks registered by this application. Note this may include
hooks installed by high level functions, such as [`record`](#mouse.record).



<a name="mouse.record"/>

## mouse.**record**(button=&#x27;right&#x27;, target\_types=(&#x27;down&#x27;,))

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L223)


Records all mouse events until the user presses the given button.
Then returns the list of events recorded. Pairs well with [`play(events)`](#mouse.play).

Note: this is a blocking function.
Note: for more details on the mouse hook and events see [`hook`](#mouse.hook).



<a name="mouse.play"/>

## mouse.**play**(events, speed\_factor=1.0, include\_clicks=True, include\_moves=True, include\_wheel=True)

[\[source\]](https://github.com/boppreh/mouse/blob/master/mouse/__init__.py#L237)


Plays a sequence of recorded events, maintaining the relative time
intervals. If speed_factor is <= 0 then the actions are replayed as fast
as the OS allows. Pairs well with [`record()`](#mouse.record).

The parameters `include_*` define if events of that type should be inluded
in the replay or ignored.



<a name="mouse.replay"/>

## mouse.**replay**

Alias for [`play`](#mouse.play).


