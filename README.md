AnyDesk Tool Kit es un proyecto de código abierto disponible para descarga y modificación libre. Como herramienta open-source, puedes usarla, modificarla y mejorarla según tus necesidades o preferencias, ya sea para uso personal o profesional.

Descripción
AnyDesk Tool Kit es una herramienta complementaria para el control y configuración rápida de AnyDesk, diseñada para usuarios que requieren gestionar configuraciones de acceso remoto de manera eficiente. A través de una interfaz gráfica intuitiva, puedes establecer o eliminar contraseñas de acceso, abrir AnyDesk, y ajustar configuraciones de seguridad, todo desde una sola aplicación.


1. ¿Qué es AnyDesk Tool Kit y para qué sirve?

Este proyecto permite:
- Control de Contraseñas: Establecer o eliminar contraseñas en AnyDesk para mejorar la seguridad del acceso remoto.

- Acceso Rápido: Abrir AnyDesk directamente desde la aplicación.

- Gestión de Configuración: Configurar opciones y guardar contraseñas en una base de datos local para asegurar el control de acceso.

Es especialmente útil para personas que necesitan controlar remotamente dispositivos a través de AnyDesk y buscan una solución que permita configurar y gestionar opciones de acceso de forma sencilla.


2. ¿Cómo se utiliza?
   
- Iniciar la aplicación: Al abrirla, se carga una interfaz gráfica con botones para cada función principal.

- Establecer o eliminar una contraseña: Usa los botones dedicados para crear o eliminar una contraseña de acceso para AnyDesk.

- Abrir AnyDesk: Inicia AnyDesk desde la propia aplicación con un clic.

- Configuración de contraseña: En la sección de Configuración, puedes guardar o actualizar la contraseña. La app incluye opciones para mostrar y ocultar la contraseña durante su configuración.


3. ¿Cómo se compila?
   
- Clonar el repositorio: git clone https://github.com/tu_usuario/anydesk-tool-kit.git
- cd anydesk-tool-kit
- Instalar dependencias: pip install -r requirements.txt
Ejecutar la aplicación: python main.py

4. Crear .EXE para despliegue en producción
Para generar un archivo ejecutable (.exe) de AnyDesk Tool Kit y facilitar su distribución como una aplicación independiente, sigue estos pasos:

Ejecutar el comando de compilación:

Comando: "flet build windows --verbose"

Este comando compilará el proyecto en un ejecutable de Windows, ideal para entornos de producción.

![anykit py](https://github.com/user-attachments/assets/276ec3f9-320b-4df4-a028-24384152f00c)


