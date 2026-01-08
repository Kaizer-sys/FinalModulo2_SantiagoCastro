import functools
from abc import ABC, abstractmethod
from datetime import date

def firma_santiago(func):
    """Sello de Santiago"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[SISTEMA SANTIAGO] Ejecutando: {func.__name__.upper()}...")
        return func(*args, **kwargs)
    return wrapper

def imprimir_banner():
        banner = f"""
        {'='*45}
        SISTEMA DE GESTIÓN DE TRANSPORTE SEGURO S.A.
        Desarrollado por: SANTIAGO
        Fecha: {date.today()}
        {'='*45}
        """
        print(banner)


class Motor:
    def __init__(self, serial, cilindraje):
        self.serial = serial
        self.cilindraje = cilindraje

class Conductor:
    def __init__(self, nombre, documento, licencia):
        self.nombre = nombre
        self.documento = documento
        self.licencia = licencia

class Vehiculo(ABC):
    def __init__(self, placa, modelo, serial_motor, cilindraje):
        self.placa = placa
        self.modelo = modelo
        self.motor = Motor(serial_motor, cilindraje)
        self.conductor = None

    def asignar_conductor(self, conductor):
        self.conductor = conductor
        print(f"✅ Conductor {conductor.nombre} asignado a {self.placa}")

    @abstractmethod
    def validar_requisitos(self):
        pass

    @firma_santiago
    def iniciar_jornada(self):
        if not self.conductor:
            print(f"❌ ERROR: El vehículo {self.placa} no tiene conductor.")
            return False
        
        if self.validar_requisitos():
            print(f"🚀 JORNADA EXITOSA: {self.placa} listo para operar.")
            return True
        return False

# --- Subclases Especializadas ---

class Moto(Vehiculo):
    def __init__(self, placa, modelo, serial_motor, cilindraje, tiene_casco):
        super().__init__(placa, modelo, serial_motor, cilindraje)
        self.tiene_casco = tiene_casco

    def validar_requisitos(self):
        if not self.tiene_casco:
            print(f"⚠️ BLOQUEO: La moto {self.placa} requiere casco obligatorio.")
            return False
        return True

class Carro(Vehiculo):
    def __init__(self, placa, modelo, serial_motor, cilindraje, vence_tecnico):
        super().__init__(placa, modelo, serial_motor, cilindraje)
        self.vence_tecnico = vence_tecnico

    def validar_requisitos(self):
        if self.vence_tecnico < date.today():
            print(f"⚠️ BLOQUEO: Carro {self.placa} con revisión técnico-mecánica vencida.")
            return False
        return True

class Camion(Vehiculo):
    def __init__(self, placa, modelo, serial_motor, cilindraje, planilla_ok):
        super().__init__(placa, modelo, serial_motor, cilindraje)
        self.planilla_ok = planilla_ok

    def validar_requisitos(self):
        if not self.planilla_ok:
            print(f"⚠️ BLOQUEO: Camión {self.placa} no cuenta con planilla de carga.")
            return False
        return True
    

if __name__ == "__main__":
    imprimir_banner()

    # 1. Instanciando Datos
    santiago_dev = Conductor("Santiago", "ID-999", "A2-B1")
    mi_moto = Moto("STG-001", 2024, "MOT-X", 500, tiene_casco=True)
    mi_carro = Carro("STG-777", 2023, "ENG-44", 1600, vence_tecnico=date(2025, 12, 31))
    mi_camion = Camion("STG-999", 2022, "TRUCK-Z", 5000, planilla_ok=False)
    
    # 2. Operación
    print("--- PROCESANDO MOTO ---")
    mi_moto.asignar_conductor(santiago_dev)
    mi_moto.iniciar_jornada()

    print("\n--- PROCESANDO CARRO ---")
    mi_carro.asignar_conductor(santiago_dev)
    mi_carro.iniciar_jornada()
    
    print("\n--- PROCESANDO CAMIÓN ---")
    mi_camion.asignar_conductor(santiago_dev)
    mi_camion.iniciar_jornada()
    