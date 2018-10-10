pygame_note.java

// links:

// examples
https://github.com/pygame/pygame/tree/master/examples


// tut

https://www.jianshu.com/p/cb146af64f05


https://dr0id.bitbucket.io/legacy/pygame_tutorials.html


http://programarcadegames.com/?chapter=example_code

http://pygametutorials.wikidot.com/tutorials-basic

http://thepythongamebook.com/en:pygame:start



// run example:
python3 -m pygame.examples.aliens

--------------------------
[main field]




Surface obj 
	represents image 

	pygame.image.load()
	BMP, JPG, PNG, TGA, and GIF

Rect obj 
	Rect(x, y, width, height) -> Rect

	0,0		10,0

	0,10	10,10

pygame.display.set_mode() //初始化游戏显示窗口
pygame.display.update() //刷新屏幕内容显示，稍后使用
set_mode 
	set_mode(resolution=(0,0),flags=0,depth=0)->Surface

// draw the whole screen
 pygame.display.flip()



cdrom			playback
cursors			load cursor images, includes standard cursors
display			control the display window or screen
draw			draw simple shapes onto a Surface
event			manage events and the event queue
font			create and render TrueType fonts
image			save and load images
joystick			manage joystick devices
key			manage the keyboard
mouse			manage the mouse
sndarray			manipulate sounds with numpy
surfarray			manipulate images with numpy
time			control timing
transform			scale, rotate, and flip images
--------------------------
--------------------------
--------------------------
--------------------------