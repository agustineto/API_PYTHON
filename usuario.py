class Usuario:
    def constructor(self,
                 nombre, apellidop, apellidom,
                 fec_nacimiento, edo_nacimiento, nvl_estudios,
                 genero, correo, password, movil, foto_perfil):
        self.nombre = nombre
        self.apellidop = apellidop
        self.apellidom = apellidom
        self.fec_nacimiento = fec_nacimiento
        self.edo_nacimiento = edo_nacimiento
        self.nvl_estudios = nvl_estudios
        self.genero = genero
        self.correo = correo
        self.password = password
        self.movil = movil
        self.foto_perfil = foto_perfil

    def login(self, correo, password):
        self.correo = correo
        self.password = password