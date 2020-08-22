import processing.svg.*;
void setup() {
	noStroke();
	background(0,0,0);
	noLoop();
// 	size(800, 800);
	size(800, 800, SVG, "AppIcon.svg");
}
void draw(){
	fill(0,56,168,255);
	triangle(width,height/3,10*width/12,2*height/9,width/4,height/2);
	fill(155,79,150,255);
	triangle(width/2,0,width/4,height/6,width,height/3);
	fill(214,2,112,255);
	triangle(0,height,width/2,0,width/4,height/6);
}
