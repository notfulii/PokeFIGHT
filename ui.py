import pygame
import settings


def load_image(path, width, height):
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image


def load_icon(path, max_size):
    image = pygame.image.load(path).convert_alpha()

    visible_area = image.get_bounding_rect()
    image = image.subsurface(visible_area).copy()

    biggest_side = max(image.get_width(), image.get_height())
    factor = max_size / biggest_side
    new_width = int(image.get_width() * factor)
    new_height = int(image.get_height() * factor)

    return pygame.transform.smoothscale(image, (new_width, new_height))


def draw_icon_button(screen, rect, icon, color):
    draw_button_box(screen, rect, color)

    icon_x = rect.centerx - icon.get_width() // 2
    icon_y = rect.centery - icon.get_height() // 2
    screen.blit(icon, (icon_x, icon_y))


def draw_text(screen, font, text, x, y, color=settings.TEXT_COLOR):
    shadow = font.render(text, False, settings.SHADOW_COLOR)
    words = font.render(text, False, color)
    screen.blit(shadow, (x + settings.SHADOW_OFFSET, y + settings.SHADOW_OFFSET))
    screen.blit(words, (x, y))


def draw_centered_text(screen, font, text, center_x, y, color=settings.TEXT_COLOR):
    text_width = font.size(text)[0]
    x = center_x - text_width // 2
    draw_text(screen, font, text, x, y, color)


def draw_person_shape(screen, color, x, y, size, extra):
    head_radius = size // 4 + extra
    head_center = (x, y + size // 4)
    pygame.draw.circle(screen, color, head_center, head_radius)

    body_width = size + extra * 2
    body_height = size // 2 + extra * 2
    body_x = x - body_width // 2
    body_y = y + size // 2 + 2 - extra
    body = pygame.Rect(body_x, body_y, body_width, body_height)
    pygame.draw.rect(screen, color, body, border_top_left_radius=body_width // 2, border_top_right_radius=body_width // 2)


def draw_person(screen, color, x, y):
    size = settings.PERSON_SIZE
    draw_person_shape(screen, settings.PERSON_OUTLINE_COLOR, x, y, size, settings.PERSON_OUTLINE_WIDTH)
    draw_person_shape(screen, color, x, y, size, 0)


def draw_button_box(screen, rect, color):
    mouse_position = pygame.mouse.get_pos()

    if rect.collidepoint(mouse_position):
        border_color = settings.HOVER_COLOR
    else:
        border_color = settings.BUTTON_BORDER_COLOR

    pygame.draw.rect(screen, color, rect, border_radius=settings.BUTTON_RADIUS)
    pygame.draw.rect(screen, border_color, rect, settings.BUTTON_BORDER_WIDTH, border_radius=settings.BUTTON_RADIUS)


def draw_button(screen, font, rect, label, color):
    draw_button_box(screen, rect, color)

    text_y = rect.centery - font.get_height() // 2
    draw_centered_text(screen, font, label, rect.centerx, text_y)
