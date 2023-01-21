biblioteca = {
      'categorias':['terror','SF','aventuras'],
      'users':['admin','estudiante1','estudiante2'],
      'libros': {
          'A01': {'Titulo':"Dune",
                  'Autor': "Frank Herbert",
                  'categoria': 'SF',
                  'estado':[]
                  },
          'B02': {'Titulo':"Dracula",
                  'Autor': "Brank Stoker",
                  'categoria': 'terror',
                  'estado':[]
                  },
          'C03': {'Titulo':"Tom Sawyer",
                  'Autor': "Mark Twain",
                  'categoria': 'aventuras',
                  'estado':[""]
                  }     
              }
    }
        ##ver lista de usuarios de la biblioteca
usuariosExistentes=biblioteca['users']
usuarioAgregar=input("que usuario es admin o estudiante: ")
if usuarioAgregar in usuariosExistentes:
  print("usuario existente")
  print(biblioteca["users"])
  if usuarioAgregar == 'admin':
    print("MENU")
    print(" 1. Listado de categoria disponibles ")
    print(" 2. Listado de libros")
    op= int(input("Que accion desea realizar:"))
    if op==1:
      print(biblioteca["categorias"])
    elif op== 2:
      listCodLibro= list(biblioteca['libros'].keys())
      print(listCodLibro)
      codLibro =input("ingrese codigo de libro:")
    if codLibro in listCodLibro:
      print(biblioteca['libros'][codLibro])
      msg=input("se presto el libro ? s o n")
    if msg == 's':
      cambioEstado = input("Diponible o Prestado")
      biblioteca['libros'][codLibro]['estado'].insert(0,cambioEstado)
      print("-----------se realizo el cambio --------------")
      print(biblioteca['libros'][codLibro])
                
  else:
    biblioteca['users'].append(usuarioAgregar)
    print(biblioteca["users"])