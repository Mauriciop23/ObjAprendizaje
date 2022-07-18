from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class objeto(models.Model):
    idobjeto = models.AutoField(primary_key=True)
    archivo = models.FileField(upload_to='objetos/', max_length=150, blank=True, null=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    estatus = models.CharField(max_length=45)
    fecha = models.DateField(blank=True, null=True)
    calificacionfinal = models.FloatField(blank=True, null=True)
    precio = models.FloatField(blank=True, null=True) 
    descargas = models.IntegerField(blank=True, null=True) 
     
    def __str__(self):
        return self.idobjeto
    
    class Meta:
        managed = True
        db_table = 'objeto'

class area(models.Model):
    idarea = models.AutoField(primary_key=True)
    idobjeto = models.ForeignKey('objeto', models.DO_NOTHING, db_column='idobjeto')
    nombre = models.CharField(max_length=45)
     
    def __str__(self):
        return self.idarea
    
    class Meta:
        managed = True
        db_table = 'area'      

class autor(models.Model):
    idautor = models.AutoField(primary_key=True)
    idobjeto = models.ForeignKey('objeto', models.DO_NOTHING, db_column='idobjeto')
    username = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='username')
     
    def __str__(self):
        return self.idautor
    
    class Meta:
        managed = True
        db_table = 'autor'           

class comentario(models.Model):
    idcomentario = models.AutoField(primary_key=True)
    idobjeto = models.ForeignKey('objeto', models.DO_NOTHING, db_column='idobjeto')
    comentario = models.CharField(max_length=45)
    username = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='username')
     
    def __str__(self):
        return self.idcomentario
    
    class Meta:
        managed = True
        db_table = 'comentario'    

class calificacion(models.Model):
    idcalificacion = models.AutoField(primary_key=True)
    idobjeto = models.ForeignKey('objeto', models.DO_NOTHING, db_column='idobjeto')
    calificacion = models.FloatField(blank=True, null=True)
    username = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='username')
     
    def __str__(self):
        return self.idcalificacion
    
    class Meta:
        managed = True
        db_table = 'calificacion'            

##############################  USUARIOS #######################################        

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,telefono,rfc,institucion,departamento,estado,carrera,semestre,password = None):
        if not email:
            raise ValueError('Favor de ingresar un correo electrónico!')

        usuario = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombres = nombres, 
            apellidos = apellidos,
            telefono = telefono,
            rfc = rfc,
            institucion = institucion,
            departamento = departamento,
            estado = estado,
            carrera = carrera,
            semestre = semestre
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,email,username,nombres,apellidos,password,telefono,rfc,institucion=None,departamento=None,estado=None,carrera=None,semestre=None):
        usuario = self.create_user(
            email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            telefono=telefono,
            rfc=rfc,
            institucion=institucion,
            departamento=departamento,
            estado=estado,
            carrera=carrera,
            semestre=semestre,
            password=password
        )
        usuario.rol = "admin"
        usuario.save()
        return usuario
    
    def create_profesor_user(self,email,username,nombres,apellidos,password,telefono,rfc,institucion,departamento,estado=None,carrera=None,semestre=None):
        usuario = self.create_user(
            email=email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            telefono=telefono,
            rfc=rfc,
            institucion=institucion,
            departamento=departamento,
            estado=estado,
            carrera=carrera,
            semestre=semestre,
            password=password
        )
        usuario.rol = "profesor"
        usuario.save()
        return usuario

    def create_alumno_user(self,email,username,nombres,apellidos,password,telefono,institucion,estado,carrera,semestre,rfc=None,departamento=None):
        usuario = self.create_user(
            email=email,
            username=username,
            nombres=nombres,
            apellidos=apellidos,
            telefono=telefono,
            rfc=rfc,
            institucion=institucion,
            departamento=departamento,
            estado=estado,
            carrera=carrera,
            semestre=semestre,
            password=password
        )
        usuario.rol = "alumno"
        usuario.save()
        return usuario    

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario', max_length = 100, unique=True)
    email = models.EmailField('Correo Electronico', max_length = 254, unique = True)
    nombres = models.CharField('Nombres', max_length = 200, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length = 200, blank = True, null = True)
    usuario_activo = models.BooleanField(default=True)
    telefono = models.CharField('Telefono', max_length=45, blank=True, null=True)
    rfc = models.CharField('RFC', max_length = 200, blank = True, null = True)
    institucion = models.CharField('Institucion', max_length = 200, blank = True, null = True)
    departamento = models.CharField('Departamento', max_length = 200, blank = True, null = True)
    estado = models.CharField('Estado', max_length = 200, blank = True, null = True)
    carrera = models.CharField('Carrera', max_length = 200, blank = True, null = True)
    semestre = models.IntegerField('Semestre', blank = True, null = True)
    rol = models.CharField('Rol', max_length=40)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres', 'apellidos', 'telefono', 'rfc']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True
    

    @property
    def is_staff(self):
        return self.rol        