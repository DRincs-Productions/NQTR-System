define gui.lateralframescroll_ysize = 850
define gui.little_text_size = 18
define gui.normal_text_size = 24
define gui.big_normal_text_size = 28
define gui.hour_text_size = 60

image gui triangular_button = "/interface/button/triangular_button.webp"

style menu_vscroll is vscrollbar:
    xsize 7
    unscrollable 'hide'

init:
    transform middle_room:
        size (136, 136)
        on selected_idle:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 1 alpha 0.9 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 1 alpha 0.9 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 alpha 0.9 matrixcolor BrightnessMatrix(-0.5)
    transform small_map:
        size (80, 80)
        on selected_idle:
            yanchor 0 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 1 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 1 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform middle_action:
        size (120, 120)
        on selected_idle:
            yanchor 0 alpha 0.7
        on idle:
            yanchor 0 alpha 0.7
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform middle_action_is_in_room:
        on selected_idle:
            yanchor 0 matrixcolor BrightnessMatrix(-0.3)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.1)
        on selected_hover:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform small_face:
        size (60, 60)
        on selected_idle:
            yanchor 0 alpha 1.0
        on idle:
            yanchor 0 alpha 1.0
        on hover:
            yanchor 1 alpha 0.93
        on selected_hover:
            yanchor 1 alpha 0.93
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform small_menu:
        size (80, 80)
        on selected_idle:
            yanchor 0 alpha 0.4
        on idle:
            yanchor 0 alpha 0.4
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform small_menu_mobile:
        size (100, 100)
        on selected_idle:
            yanchor 0 alpha 0.4
        on idle:
            yanchor 0 alpha 0.4
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
    transform close_zoom:
        xanchor 25
        size (75, 25)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.9)
    transform close_zoom_mobile:
        xanchor 35
        size (105, 35)
        on idle:
            yanchor 0 matrixcolor BrightnessMatrix(0)
        on hover:
            yanchor 0 matrixcolor BrightnessMatrix(0.9)
    transform middle_map(rotation = 0, xsize = 50, ysize = 50):
        rotate rotation
        xysize (xsize, ysize)
        on selected_idle:
            yanchor 0 alpha 0.6
        on idle:
            yanchor 0 alpha 0.6
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
        on insensitive:
            yanchor 0 matrixcolor BrightnessMatrix(-0.8)
        on action:
            yanchor 0 matrixcolor BrightnessMatrix(-0.5)
