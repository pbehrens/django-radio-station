animatedcollapse.addDiv('about', 'fade=0,speed=400,group=srv,hide=1')
animatedcollapse.addDiv('blog', 'fade=0,speed=400,group=srv,hide=1')
animatedcollapse.addDiv('events', 'fade=0,speed=400,group=srv,hide=1')

animatedcollapse.ontoggle=function($, divobj, state){ //fires each time a DIV is expanded/contracted
// $(divobj)
//divobj: DOM reference to DIV being expanded/ collapsed. Use "divobj.id" to get its ID
//state: "block" or "none", depending on state
}

animatedcollapse.init()
		
		
		
		
		
