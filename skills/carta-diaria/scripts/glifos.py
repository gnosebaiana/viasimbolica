"""Ícones em traço (viewBox 0 0 24 24) do Sol, da Lua e dos doze signos.

Desenhados no mesmo traço da estrela cadente: linha de 1,5, pontas redondas,
sem preenchimento (o ponto do Sol é a única parte cheia).
"""

SOL = '<circle cx="12" cy="12" r="8.6"/><circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none"/>'
LUA = '<path d="M15.5 3.6A8.8 8.8 0 1 0 15.5 20.4A7.2 8.8 0 0 1 15.5 3.6Z"/>'

SIGNOS = [
    ("Áries", '<path d="M12 21V10c0-4.5-2.2-6.5-4.6-6.5S3.5 5.4 3.5 8M12 10c0-4.5 2.2-6.5 4.6-6.5S20.5 5.4 20.5 8"/>'),
    ("Touro", '<circle cx="12" cy="15" r="5.5"/><path d="M4 3.5c1.5 3.6 4.5 6 8 6s6.5-2.4 8-6"/>'),
    ("Gêmeos", '<path d="M5 4c4 1.6 10 1.6 14 0M5 20c4-1.6 10-1.6 14 0M9.2 5.2v13.6M14.8 5.2v13.6"/>'),
    ("Câncer", '<circle cx="7" cy="9.2" r="2.6"/><path d="M4.4 9.2C4.4 6 7.8 3.6 12 3.6c4 0 7 1.3 8.5 3"/><circle cx="17" cy="14.8" r="2.6"/><path d="M19.6 14.8c0 3.2-3.4 5.6-7.6 5.6-4 0-7-1.3-8.5-3"/>'),
    ("Leão", '<circle cx="7" cy="15.5" r="3"/><path d="M10 15.5c0-4-3-6-3-9.3a4.5 4.5 0 0 1 9 0c0 4.2-3.5 7.6-3.5 11.5 0 1.9 1.2 2.8 2.7 2.8s2.8-1 2.8-2.6"/>'),
    ("Virgem", '<path d="M3 7.5V18M3 10c0-3.4 5-3.4 5 0v8M8 10c0-3.4 5-3.4 5 0v7c0 2.5 1.5 3.6 3.5 3.2M13 13.5c2.4-2.6 6.6-1.9 6.2 1.3-.3 2.6-3.6 4.4-7.4 5.7"/>'),
    ("Libra", '<path d="M3 20h18M3 16h5.4a4.4 4.4 0 1 1 7.2 0H21"/>'),
    ("Escorpião", '<path d="M3 7.5V18M3 10c0-3.4 5-3.4 5 0v8M8 10c0-3.4 5-3.4 5 0v8.2c0 1.6.9 2.3 2.4 2.3H20M17.6 18.2l2.6 2.3-2.6 2.3"/>'),
    ("Sagitário", '<path d="M4 20L20 4M12.5 4H20v7.5M7 11.5l5.5 5.5"/>'),
    ("Capricórnio", '<path d="M3 6.5c1.6 0 2.6 1.2 3 3l2.6 10 3-12c.8-3 5.3-2.8 5.3.7 0 2.6-1 5-2 7.2M14.9 15.4c.9-1.7 4.6-1.7 4.6 1.2 0 2.2-1.9 3.1-3.4 3.1-1.7 0-2.8-1.3-3.8-2.9"/>'),
    ("Aquário", '<path d="M2.5 10.2l3.2-3.2 3.2 3.2 3.2-3.2 3.2 3.2 3.2-3.2 3.2 3.2M2.5 17.4l3.2-3.2 3.2 3.2 3.2-3.2 3.2 3.2 3.2-3.2 3.2 3.2"/>'),
    ("Peixes", '<path d="M5 3.5c3.6 4.5 3.6 12.5 0 17M19 3.5c-3.6 4.5-3.6 12.5 0 17M4.5 12h15"/>'),
]


def svg(corpo: str) -> str:
    return f'<svg class="gl" viewBox="0 0 24 24" aria-hidden="true">{corpo}</svg>'
