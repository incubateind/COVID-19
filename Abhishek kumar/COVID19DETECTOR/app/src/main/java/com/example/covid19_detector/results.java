package com.example.covid19_detector;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class results extends AppCompatActivity {
diagnosis diag = new diagnosis();
    TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_results);

        int risk = Math.abs(diag.result - 1)/10;
        TextView textView = findViewById(R.id.tvresults);

if (risk <= 0.3){
    textView.setText("You may have stress related issue. It would be better to observe and wait");
}
else
    if(risk <= 0.6){
        textView.setText("There is a chance you have dehydration. It would be advisable to hydrate properly and in case conditoins worsen, do seek consultation with a doctor");
    }
    else
        if(risk <= 0.8){
            textView.setText("It's advisable to consult a doctor asap");
        }
        else
            textView.setText("Do a COVID-19 test immidiately");

    }


}
