from ..modelos.estudiantes import *
from .conexion import connect
from sqlmodel import SQLModel, Session, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

# a partir de qui generamos el ORM del proyecto
def select_all():
    # crear una lista de estudiantes
    engine = connect()
    with Session(engine) as session:
        consulta = select(AsignaturaPeriodo).options(selectinload(AsiganturaPeriodo.estudiante))
        asignatura_periodo = session.exec(consulta)
        return asignatura_periodo.all()

# buscar AsignaturaPeriodo por numero de cedula
def select_by_codigo(codigo:str):
    engine = connect()
    with Session(engine) as session:
        consulta = select(AsiganturaPeriodo).where(AsiganturaPeriodo.codigo == codigo)
        resultado = session.exec(consulta)
        return resultado.all()

# crear un asignatura_periodo
def crear_asignatura_periodo(asignatura_periodo: AsiganturaPeriodo):
    engine = connect()
    try:
        with Session(engine) as session:
            session.add(asignatura_periodo)
            session.commit()
            print(asignatura_periodo)
            if asignatura_periodo.id is not None:
                consulta = select(AsiganturaPeriodo).where(AsiganturaPeriodo.id == asignatura_periodo.id)
                resultado = session.exec(consulta)
                return resultado.all()
            else:
                return None
    except SQLAlchemyError as e:
        print(e)

# eliminar asignatura_periodo
def eliminar_asignatura_periodo(id : int):
    engine = connect()
    try:
        with Session(engine) as session:
            consulta = select(AsiganturaPeriodo).where(AsiganturaPeriodo.id == id)
            objeto = session.exec(consulta).one_or_none()
            if objeto:
                session.delete(objeto)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        print(e)

# actualizar registro
def actualizar_asignatura_periodo(asignatura_periodo: AsiganturaPeriodo):
    engine = connect()
    try:
        with Session(engine) as session:
            consulta = select(AsiganturaPeriodo).where(AsiganturaPeriodo.id == objeto.id)
            objeto_actual = session.exec(consulta).one_or_none()
            if objeto_actual:
                session.update(objeto_actual)
                session.commit()
                return True
            else:
                return False
    except SQLAlchemyError as e:
        print(e)
