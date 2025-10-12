package utn.tienda_libros.servicio;
import org.hibernate.persister.entity.SingleTableEntityPersister;
import utn.tienda_libros.modelo.Libro;

import java.util.List;

public interface ILibroServicio {
    public List<Libro> listarLibros();
    public Libro buscarLibroPoriD(Integer idLibro);
    public void guardarLibro(Libro libro);
    public void eliminarLibro(Libro libro);
}
