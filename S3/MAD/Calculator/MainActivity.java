package com.example.calculator;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    private EditText input;
    private String currentOperator = "";
    private double firstValue = Double.NaN;
    private boolean isOperatorPressed = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize the input field
        input = findViewById(R.id.input);
        if (input == null) {
            throw new NullPointerException("EditText input not found. Check your layout file for the correct ID.");
        }

        // Create number click listener
        View.OnClickListener numberClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Button button = (Button) v;
                if (isOperatorPressed || "Error".equals(input.getText().toString())) {
                    input.setText("");
                }
                isOperatorPressed = false;
                input.append(button.getText());
            }
        };

        // Create operator click listener
        View.OnClickListener operatorClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Button button = (Button) v;
                if (input.getText().toString().isEmpty() || "Error".equals(input.getText().toString())) {
                    return;
                }
                try {
                    firstValue = Double.parseDouble(input.getText().toString());
                } catch (NumberFormatException e) {
                    input.setText("Error");
                    return;
                }
                currentOperator = button.getText().toString();
                isOperatorPressed = true;
            }
        };

        // Register number buttons
        setupButtonClickListener(R.id.button0, numberClickListener);
        setupButtonClickListener(R.id.button1, numberClickListener);
        setupButtonClickListener(R.id.button2, numberClickListener);
        setupButtonClickListener(R.id.button3, numberClickListener);
        setupButtonClickListener(R.id.button4, numberClickListener);
        setupButtonClickListener(R.id.button5, numberClickListener);
        setupButtonClickListener(R.id.button6, numberClickListener);
        setupButtonClickListener(R.id.button7, numberClickListener);
        setupButtonClickListener(R.id.button8, numberClickListener);
        setupButtonClickListener(R.id.button9, numberClickListener);

        // Register operator buttons
        setupButtonClickListener(R.id.buttonAdd, operatorClickListener);
        setupButtonClickListener(R.id.buttonSubtract, operatorClickListener);
        setupButtonClickListener(R.id.buttonMultiply, operatorClickListener);
        setupButtonClickListener(R.id.buttonDivide, operatorClickListener);

        // Clear button
        setupButtonClickListener(R.id.buttonClear, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                input.setText("");
                currentOperator = "";
                firstValue = Double.NaN;
            }
        });

        // Equals button
        setupButtonClickListener(R.id.buttonEquals, new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (input.getText().toString().isEmpty() || Double.isNaN(firstValue)) {
                    return;
                }

                double secondValue;
                try {
                    secondValue = Double.parseDouble(input.getText().toString());
                } catch (NumberFormatException e) {
                    input.setText("Error");
                    return;
                }

                double result = 0;
                switch (currentOperator) {
                    case "+":
                        result = firstValue + secondValue;
                        break;
                    case "-":
                        result = firstValue - secondValue;
                        break;
                    case "*":
                        result = firstValue * secondValue;
                        break;
                    case "/":
                        if (secondValue != 0) {
                            result = firstValue / secondValue;
                        } else {
                            input.setText("Error");
                            return;
                        }
                        break;
                    default:
                        input.setText("Error");
                        return;
                }

                input.setText(String.valueOf(result));
                currentOperator = "";
                firstValue = Double.NaN;
                isOperatorPressed = true;
            }
        });
    }

    // Helper method to setup button click listeners safely
    private void setupButtonClickListener(int buttonId, View.OnClickListener listener) {
        Button button = findViewById(buttonId);
        if (button == null) {
            throw new NullPointerException("Button with ID " + buttonId + " not found. Check your layout file.");
        }
        button.setOnClickListener(listener);
    }
}
