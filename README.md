# Prueba Tecnica - Finkargo

## Descripción general
El objetivo de esta API es proporcionar servicios bajo una arquitectura RESTful. A continuación se describen los endpoints disponibles y su funcionalidad.

## Endpoint 1: Ordenar Matriz de Números

### Descripción
Este endpoint recibe una matriz de números y devuelve la misma matriz ordenada, teniendo en cuenta que los números duplicados se deben mover al final de la lista ordenada.

#### Endpoint
`GET /sort`

#### Parámetros de entrada
El endpoint espera recibir un objeto JSON con la siguiente estructura:

```json
{
  "sin clasificar": [3, 5, 5, 6, 8, 3, 4, 4, 7, 7, 1, 1, 2]
}
```

#### Respuesta
Si la petición es exitosa, la API responderá con un objeto JSON que contiene la matriz sin clasificar y la matriz clasificada:

```json
{
  "sin clasificar": [3, 5, 5, 6, 8, 3, 4, 4, 7, 7, 1, 1, 2],
  "clasificado": [1, 2, 3, 4, 5, 6, 7, 8, 5, 3, 4, 7, 1]
}
```

## Endpoint 2: Balance de Ventas y Gastos

### Descripción
Este endpoint recibe un diccionario con información sobre ventas y gastos por mes. Devuelve un JSON con la información anterior e incluye el balance de cada mes.

#### Endpoint
`GET /balance`

#### Parámetros de entrada
El endpoint espera recibir un objeto JSON con la siguiente estructura:

```json
{
  "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
  "Ventas": [30500, 35600, 28300, 33900],
  "Gastos": [22000, 23400, 18100, 20700]
}
```

#### Respuesta
Si la petición es exitosa, la API responderá con un objeto JSON que contiene la información del mes, las ventas, los gastos y el balance:

```json
{
  "mes": "Enero",
  "Ventas": 30500,
  "Gastos": 35600,
  "Balance": -5100
}
```

## Endpoint 3: Gestión de Usuarios

### Descripción
Este endpoint permite gestionar la información de los usuarios en una base de datos. Se deben implementar las operaciones de añadir, consultar, modificar y eliminar la información de un usuario.

#### Endpoint

- **Añadir usuario**: `POST /users`

  Añade un nuevo usuario a la base de datos.

- **Consultar usuario**: `GET /users`

  Obtiene la información de todos los usuarios.

- **Consultar usuario**: `GET /users/{id}`

  Obtiene la información de un usuario específico.

- **Modificar usuario**: `PUT /users/{id}`

  Modifica la información de un usuario existente.

- **Eliminar usuario**: `DELETE /users/{id}`

  Elimina un usuario de la base de datos.

## Endpoint 4: Login mediante Basic Auth

### Descripción
La autenticación se realiza mediante el encabezado de solicitud `Authorization` con el esquema de autenticación básica. El valor del encabezado debe ser de la forma `Basic {credenciales_base64}`, donde `{credenciales_base64}` es el nombre de usuario y la contraseña codificados en Base64.

#### Respuesta
Si las credenciales son válidas, la API responderá con un código de respuesta HTTP 200 (OK). En caso contrario, se devolverá un código de respuesta HTTP 401 (Unauthorized).

## Consideraciones generales

¡Gracias por utilizar nuestra API! Si tienes alguna pregunta o necesitas más información, no dudes en contactarnos.