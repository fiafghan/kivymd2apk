from kivy.animation import Animation

def animation(widget_name, size_hint, duration):
    animation = Animation(
                size_hint = size_hint,  # Target position
                duration=duration,  # Animation duration in seconds
                t="out_elastic"  # Easing function
            )
    animation.start(widget_name)