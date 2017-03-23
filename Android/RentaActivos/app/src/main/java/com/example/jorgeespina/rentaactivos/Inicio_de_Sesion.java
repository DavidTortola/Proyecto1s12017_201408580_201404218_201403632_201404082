package com.example.jorgeespina.rentaactivos;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.Toast;

public class Inicio_de_Sesion extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_inicio_de__sesion);
        ImageButton  boton = (ImageButton) findViewById(R.id.ingresar);
        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String usuario = ((EditText)findViewById(R.id.txtusuario)).getText().toString();
                String contraseña = ((EditText)findViewById(R.id.txtcontraseña)).getText().toString();
                if (usuario.equals("admin")&& contraseña.equalsIgnoreCase(("admin"))){
                    Intent nuevoform = new Intent(Inicio_de_Sesion.this,Secundaria.class);
                    startActivity(nuevoform);

                }else{
                    Toast.makeText(getApplicationContext(),"Usuario Incorrecto",Toast.LENGTH_SHORT).show();
                }
            }
        });

    }
}
