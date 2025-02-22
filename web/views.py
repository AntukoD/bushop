from django.shortcuts import render,get_object_or_404

from .models import Producto,Categoria

# Create your views here.
"""vistas para el catalogo del producto"""
def index(request):
    listaProductos = Producto.objects.all()
    listaCategoria = Categoria.objects.all()
    #print(listaProductos)

    context = {
        'productos': listaProductos,
        'categorias': listaCategoria
    }

    return render(request, 'index.html',context)

def productosPorCategoria(request,categoria_id):
    """vista para filtrar productos por categoria"""
    objCategoria = Categoria.objects.get(pk=categoria_id)
    listaProductos = objCategoria.producto_set.all()  

    listaCategorias = Categoria.objects.all()
    context = {
        'categorias': listaCategorias,
        'productos': listaProductos
        

    }
    return render(request, 'index.html',context)


def productosPorNombre(request):
    """vista para filtrar productos por nombre"""
    nombre = request.POST['nombre']
    
    listaProductos = Producto.objects.filter(nombre__icontains=nombre)
    listaCategorias = Categoria.objects.all()
    context = {
        'categorias': listaCategorias,
        'productos': listaProductos
    }
    return render(request, 'index.html',context)

##nueva vista

def productoDetalle(request,producto_id):
    """vista para filtrar productos por nombre"""
    #objProducto = Producto.objects.get(pk=producto_id)
    objProducto = get_object_or_404(Producto,pk=producto_id)
    context = {
        'producto': objProducto
    }
    return render(request, 'producto.html',context)