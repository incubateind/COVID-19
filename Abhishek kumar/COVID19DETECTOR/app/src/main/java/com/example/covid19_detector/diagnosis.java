package com.example.covid19_detector;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class diagnosis extends AppCompatActivity {

   EditText et,et1,et2,et3,et4,et5,et6,et7,et8;
    TextView tvfinall;

    int    result, count = 0 ,
            count1=0,
            count2=0,
            count3 = 0,
            count4 = 0,
            count5 = 0,
            count6 = 0,
            count7 = 0,
            count8 = 0;

String val ;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_diagnosis);
        EditText et = findViewById(R.id.et);
        EditText et1 = findViewById(R.id.et1);
        EditText et2= findViewById(R.id.et2);
        EditText et3 = findViewById(R.id.et3);
        EditText et4 = findViewById(R.id.et4);
        EditText et5 = findViewById(R.id.et5);
        EditText et6 = findViewById(R.id.et6);
        EditText et7 = findViewById(R.id.et7);
        EditText et8 = findViewById(R.id.et8);
        Button btnok = findViewById(R.id.btnok);

        final TextView tvfinall = findViewById(R.id.tvfinall);

        while(et.getText().toString().equals("yes")   || et.getText().toString().equals("YES") || et.getText().toString().equals("Yes") )
                {
                count = count+1;

            }
        while(et1.getText().toString().trim() ==  "yes" || et1.getText().toString().trim() == "YES" || et1.getText().toString().trim() == "Yes" )
        {
            count1 = count1+1;

        }
        while(et2.getText().toString().trim() ==  "yes" || et2.getText().toString().trim() == "YES" || et2.getText().toString().trim() == "Yes" )
        {
            count2 = count2+1;
        }
        while(et3.getText().toString().trim() ==  "yes" || et3.getText().toString().trim() == "YES" || et3.getText().toString().trim() == "Yes" )
        {
            count3 = count3+1;
        }
        while(et4.getText().toString().trim() ==  "yes" || et4.getText().toString().trim() == "YES" || et4.getText().toString().trim() == "Yes" )
        {
            count4 = count4+1;
        }
        while(et5.getText().toString().trim() ==  "yes" || et5.getText().toString().trim() == "YES" || et5.getText().toString().trim() == "Yes" )
        {
            count5 = count5+1;
        }
        while(et6.getText().toString().trim() ==  "yes" || et6.getText().toString().trim() == "YES" || et6.getText().toString().trim() == "Yes" )
        {
            count6 = count6+1;
        }
        while(et7.getText().toString().trim() ==  "yes" || et7.getText().toString().trim() == "YES" || et7.getText().toString().trim() == "Yes" )
        {
            count7 = count7+1;
        }
        while(et8.getText().toString().trim() ==  "yes" || et8.getText().toString().trim() == "YES" || et8.getText().toString().trim() == "Yes" )
        {
            count8 = count8+1;
        }
        result = count+count1+count2+count3+count4+count5+count6+count7+count8;
        val = Integer.toString(result);


btnok.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {

        startActivity(new Intent(diagnosis.this, results.class));



    }
});

    }
}
