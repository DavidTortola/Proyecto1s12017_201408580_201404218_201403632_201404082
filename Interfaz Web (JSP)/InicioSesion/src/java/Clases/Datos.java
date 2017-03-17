/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Clases;

/**
 *
 * @author Jorge Espina
 */
public class Datos {
    
    private String Usuario;
    private String Contraseña;
    private String Empresa;
    private String Departamento;
    
     public void setUsuario(String user){
        this.Usuario=user;
    }
    
    public void setContraseña(String pasword){
        this.Contraseña=pasword;
    }
    
    public void setEmpresa(String empresa){
        this.Empresa=empresa;
    }
    
    public void setDepartamento(String departamento){
        this.Departamento=departamento;
    }
    
    public String getUsuario(){
        return this.Usuario;
    }
    
    public String getContraseña(){
        return this.Contraseña;
    }
    
    public String getEmpresa(){
        return this.Empresa;
    }
    public String getDepartamento(){
        return this.Departamento;
    }
}
