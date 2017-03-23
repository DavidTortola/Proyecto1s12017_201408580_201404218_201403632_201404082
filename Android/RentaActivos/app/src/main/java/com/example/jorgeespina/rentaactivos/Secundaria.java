package com.example.jorgeespina.rentaactivos;

import android.app.AliasActivity;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.Toast;

/**
 * Created by Jorge Espina on 14/03/2017.
 */

public class Secundaria extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.menuprincipal);
        Button boton = (Button) findViewById(R.id.btnrentar);
        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                Intent nuevoform = new Intent(Secundaria.this,Renta_de_Activos.class);
                startActivity(nuevoform);
            }
        });
        Button boton1 = (Button) findViewById(R.id.btnregistrodevoluciones);
        boton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v1) {
                Intent nuevoform = new Intent(Secundaria.this,Registro_de_Devoluciones.class);
                startActivity(nuevoform);
            }
        });
        Button boton2 = (Button) findViewById(R.id.btncerrarsesion);
        boton2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v2) {
                Intent nuevoform = new Intent(Secundaria.this,Inicio_de_Sesion.class);
                startActivity(nuevoform);
            }
        });

    }
}
