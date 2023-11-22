class Jugador {
    constructor(nombre) {
        this.nombre = nombre;
        this.puntuacion = 0;
    }
}

class Juego {
    constructor(jugadores, panel) {
        this.jugadores = jugadores.map(nombre => new Jugador(nombre));
        this.panelActual = '_'.repeat(panel.length);
        this.panelResuelto = panel;
        this.jugadorActual = 0;
    }

    iniciarJuego() {
        console.log(`El panel a resolver es: ${this.panelActual}`);
    }

    jugarTurno() {
        let jugador = this.jugadores[this.jugadorActual];
        let adivinanza = prompt(`${jugador.nombre}, adivina una letra o resuelve el panel:`);
        if (adivinanza.length === 1) {
            this.adivinarLetra(jugador, adivinanza);
        } else {
            this.adivinarPanel(jugador, adivinanza);
        }
    }

    adivinarLetra(jugador, letra) {
        if (this.panelResuelto.includes(letra)) {
            this.panelActual = Array.from(this.panelResuelto).map((c, i) => c === letra ? letra : this.panelActual[i]).join('');
            jugador.puntuacion += Array.from(this.panelResuelto).filter(c => c === letra).length;
            console.log(`Correcto! El panel ahora es: ${this.panelActual}`);
        } else {
            console.log("Incorrecto!");
        }
    }

    adivinarPanel(jugador, adivinanza) {
        if (adivinanza === this.panelResuelto) {
            jugador.puntuacion += 10;
            this.panelActual = this.panelResuelto;
            console.log(`Correcto! ${jugador.nombre} ha resuelto el panel!`);
        } else {
            console.log("Incorrecto!");
        }
    }

    verificarResuelto() {
        return this.panelActual === this.panelResuelto;
    }

    cambiarJugador() {
        this.jugadorActual = (this.jugadorActual + 1) % this.jugadores.length;
    }

    terminarJuego() {
        let ganador = this.jugadores.reduce((max, jugador) => max.puntuacion > jugador.puntuacion ? max : jugador);
        console.log(`El ganador es ${ganador.nombre} con ${ganador.puntuacion} puntos!`);
    }
}

// Programa principal
let jugadores = ["Jugador1", "Jugador2", "Jugador3"];
let panel = "javascript";
let juego = new Juego(jugadores, panel);
juego.iniciarJuego();
while (!juego.verificarResuelto()) {
    juego.jugarTurno();
    juego.cambiarJugador();
}
juego.terminarJuego();