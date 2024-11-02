from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Vendedor,Cliente,Deportivo,Registro_Compra,Rol,Usuario
from .forms import VendedorForm,DeportivoForm,CompraForm,RolForm, ClienteForm,UsuarioForm,ClientePasswordForm,EditarUsuarioForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .decorators import role_required

def base(request):
    return render(request,'base.html')


#Listar vendedor
@login_required
@role_required('Administrador')
def listar_vendedor(request):
    vendedor=Vendedor.objects.all()
    cantidad_vendedores=Vendedor.objects.count()
    return render(request,'vendedor/listar.html',{'vendedor':vendedor,'cantVendedores':cantidad_vendedores})



#ver vendedor
@login_required
@role_required('Administrador')
def ver_vendedor(request , pk):
    vendedor = get_object_or_404(Vendedor ,pk = pk)
    return render(request , 'vendedor/ver.html',{'vendedor':vendedor})

#Crear vendedor
@login_required
@role_required('Administrador')
def crear_vendedor(request):
    if request.method=='POST':
        form=VendedorForm(request.POST)
        if form.is_valid():
            anos=int(request.POST['anos_trabajo'])
            if anos > 45 :
                return render(request,'vendedor/crear.html',
                {'form':form,'error':'Los años de trabajo no puede ser mayor a 45'})
            elif anos < 1:
                return render(request,'vendedor/crear.html',
                {'form':form,'error':'Los años de trabajo no puede ser menor 0 '})
                        
            else:    
                form.save()
                messages.add_message(request=request,level=messages.SUCCESS,message="Vendedor creado con exito")
                return redirect('listar_vendedor')
        
    else:
       form=VendedorForm()    
    return render(request,'vendedor/crear.html',{'form':form})

#Editar vendedor
@login_required
@role_required('Administrador')
def editar_vendedor(request , pk):
    vendedor=get_object_or_404(Vendedor,pk=pk)
    if request.method=='POST':
        form=VendedorForm(request.POST,instance=vendedor)
        if form.is_valid():
            form.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Datos del vendedor actulizados con exito")
            return redirect('listar_vendedor')
        else:
            return render(request,'vendedor/editar.html',{'form':form})
    else:
        form = VendedorForm(instance=vendedor)
        return render(request,'vendedor/editar.html',{'form':form})
    
#Eliminar vendedor    
@login_required
@role_required('Administrador') 
def eliminar_vendedor(request,pk):
    vendedor=get_object_or_404(Vendedor,pk=pk)
    if vendedor:
        vendedor.delete()
        return redirect('listar_vendedor')
    
    

#Lista cliente
@login_required
@role_required('Administrador')
def listar_cliente(request):
    cliente=Cliente.objects.all()
    cantidad_clientes=Cliente.objects.count()
    return render(request,'cliente/listar.html',{'cliente':cliente,'cantidadad_clientes':cantidad_clientes})

#Crear cliente
@login_required
@role_required('Administrador')
def crear_cliente(request):
    vendedor=Vendedor.objects.all()
    if request.method=='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Cliente creado con exito")
            return redirect('listar_cliente')
        else:
            for field ,errors in form.errors.items():
                label = form.fields[field].label
                for error in errors:
                    messages.error(request,f'Error en "{label} : {error}"') 
    else:
        form = ClienteForm()
    return render(request,'cliente/crear.html',{'form':form ,'vendedor':vendedor})

#Editar Cliente
@login_required
@role_required('Administrador')
def editar_cliente(request,pk):
    vendedor=Vendedor.objects.all()
    cliente = get_object_or_404(Cliente,pk = pk)
    if request.method=='POST':
        form_cliente = ClienteForm(request.POST , instance=cliente)
        if form_cliente.is_valid():
            form_cliente.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Datos del cliente actulizados con exito")
            return  redirect('listar_cliente')
        else:
            return render(request,'cliente/editar.html',{'form_cliente':form_cliente})
    else:
        form_cliente = ClienteForm(instance=cliente)
        return render(request,'cliente/editar.html',{'form_cliente':form_cliente,'vendedor':vendedor})    
    
#Eliminiar cliente
@login_required
@role_required('Administrador')
def eliminar_cliente(request, pk ):
    cliente= get_object_or_404(Cliente ,pk=pk)
    if cliente:
        cliente.delete()
    return redirect('listar_cliente')
    
@login_required
@role_required(['Administrador','Usuario'])
#Lista deportivos
def listar_deportivo(request):
    deportivo=Deportivo.objects.all()
    return render(request,'deportivo/listar.html',{'deportivo':deportivo})



#Crear deportivos
@login_required
@role_required('Administrador')
def crear_deportivo(request):
    if request.method=='POST':
        form = DeportivoForm(request.POST ,request.FILES)
        if form.is_valid():
            messages.add_message(request=request,level=messages.SUCCESS,message="Auto creado con exito")
            form.save()
            return redirect('listar_deportivo')
    else:
        form = DeportivoForm()
    return render(request,'deportivo/crear.html',{'form':form})

#Editar deportivos
@login_required
@role_required('Administrador')
def editar_deportivo(request,pk):
    deportivo = get_object_or_404(Deportivo,pk = pk)
    if request.method=='POST':
        form_deportivo = DeportivoForm(request.POST,request.FILES , instance=deportivo)
        if form_deportivo.is_valid():
            form_deportivo.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Datos actulizados con exito")
            return  redirect('listar_deportivo')
        else:
            return render(request,'deportivo/editar.html',{'form_deportivo':form_deportivo})
    else:
        form_deportivo = DeportivoForm(instance=deportivo)
        return render(request,'deportivo/editar.html',{'form_deportivo':form_deportivo})    
    
#Eliminiar deportivo
@login_required
@role_required('Administrador')
def eliminar_deportivo(request , pk ):
    deportivo= get_object_or_404(Deportivo ,pk=pk)
    if deportivo:
        deportivo.delete()
        return redirect('listar_deportivo')
    return render(request,'deportivo/eliminar.html',{'deportivo':deportivo})




#Listas Registros de las compras
@login_required
@role_required('Administrador')
def listar_compra(request):
    compra=Registro_Compra.objects.all()
    return render(request,'compra/listar.html',{'compra':compra})




#Crear Registros de la compras
@login_required
@role_required('Administrador') 
def crear_compra(request):
    cliente=Cliente.objects.all()
    deportivo=Deportivo.objects.all()
    if request.method=='POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            monto = int(request.POST['monto'])
            if monto<10000 :
                return render(request,'compra/crear.html',{'form':form ,'cliente':cliente ,
                'deportivo':deportivo,'error':'El monto no puede ser  menor a 10k'})
            elif monto > 500000:
                return render(request,'compra/crear.html',{'form':form ,'cliente':cliente ,
                'deportivo':deportivo,'error':'El monto no puede ser  mayor a 500k'})
            else:                  
                form.save()
                messages.add_message(request=request,level=messages.SUCCESS,message="Datos de la venta creado con exito")
                return redirect('listar_compra')
    else:
        form = ()    
    return render(request,'compra/crear.html',{'form':form ,'cliente':cliente ,'deportivo':deportivo})

#Editar Registros de la compra
@login_required
@role_required('Administrador')
def editar_compra(request,pk):
    cliente=Cliente.objects.all()
    deportivo=Deportivo.objects.all()
    compra = get_object_or_404(Registro_Compra,pk = pk)
    if request.method=='POST':
        compra = CompraForm(request.POST , instance=compra)
        if compra.is_valid():
            compra.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Datos de la venta actualizado con exito")
            return  redirect('listar_compra')
        else:
            return render(request,'compra/editar.html',{'compra':compra,'cliente':cliente,'deportivo':deportivo})
    else:
        compra = CompraForm(instance=compra)
        return render(request,'compra/editar.html',{'compra':compra,'cliente':cliente,'deportivo':deportivo})    

 
#Eliminiar Registros de la compra
@login_required
@role_required('Administrador')
def eliminar_compra(request , pk ):
    compra= get_object_or_404(Registro_Compra ,pk=pk)
    if compra:
        compra.delete()
        return redirect('listar_compra')
    return render(request,'compra/eliminar.html',{'compra':compra})


#Listar Rol
@login_required
@role_required('Administrador')
def listar_roles(request):
    roles = Rol.objects.all()
    success_message = request.session.pop('success_message', None)
    return render(request, 'rol/listar.html', {'roles':roles, 'success_message': success_message})

#Crear Rol
@login_required
@role_required('Administrador') 
def crear_rol(request):
    if request.method=='POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Rol creado con exito")
            return redirect('listar_rol')
    else:
        form = ()    
    return render(request,'rol/crear.html',{'form':form})

#Editar Rol de usario
@login_required
@role_required('Administrador')
def editar_rol(request,pk):
    rol = get_object_or_404(Rol,pk = pk)
    if request.method=='POST':
        form = RolForm(request.POST , instance=rol)
        if form.is_valid():
            form.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Datos del rol actualizados con exito")
            return  redirect('listar_rol')
        else:
            return render(request,'rol/editar.html',{'form':form})
    else:
        form =RolForm(instance=rol)
        return render(request,'rol/editar.html',{'form':form})
    
    
#Eliminiar Rol
@login_required
@role_required('Administrador')
def eliminar_rol(request , pk ):
    rol= get_object_or_404(Rol ,pk=pk)
    if request.method=='POST':
        rol.delete()
        return redirect('listar_rol')
    return render(request,'rol/eliminar.html',{'rol':rol})


#Listar Usarios
@login_required
@role_required('Administrador')
def listar_usario(request):
    usuario = Usuario.objects.all()
    return render(request ,'usuario/listar.html',{'usuario':usuario})

#Crear usuario
@login_required
@role_required('Administrador')
def crear_usario(request):
    roles = Rol.objects.all()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Datos del Usuario creado con exito")
            return redirect('listar_usuario')
        else:
            for field,errors in form.errors.items():
                label = form.fields[field].label
                for error in errors:
                    messages.error(request, f'Error en "{label} ": {error}')
    else:
        form = UsuarioForm()
    return render(request ,'usuario/crear.html',{'form':form , 'roles':roles})                    
        
#Editar usuario
@login_required
@role_required('Administrador')
def editar_usuario(request,pk):
    usuario = get_object_or_404(Usuario,pk = pk)
    if request.method=='POST':
        form =EditarUsuarioForm(request.POST , instance=usuario)
        if form.is_valid():
            form.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Datos del Usuario actualizado con exito")
            return  redirect('listar_usuario')
        else:
            return render(request,'usuario/editar.html',{'form':form})
    else:
        form =EditarUsuarioForm(instance=usuario)
        return render(request,'usuario/editar.html',{'form':form})
    
@login_required
@role_required('Administrador')
def eliminar_usuario(request , pk):
    usuario = get_object_or_404(Usuario ,pk = pk)
    if usuario:
        usuario.delete()
        return redirect('listar_usuario')    

#Autenticacion Login y Logout
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('base')

# Modificar Contraseña
@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = ClientePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contraseña cambiada con éxito. Por favor, vuelve a iniciar sesión.')
            logout(request)
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                label = form.fields[field].label
                for error in errors:
                    messages.error(request, f'Error en "{label}": {error}')
            return render(request, 'cambiar_contraseña.html', {'form': form})
    else:
        form = ClientePasswordForm(user=request.user)

    return render(request, 'cambiar_contraseña.html', {'form': form})

#Vista acceso_denegado 

@login_required
def acceso_denegado(request):
    return render(request,'acceso_denegado.html')     


        



