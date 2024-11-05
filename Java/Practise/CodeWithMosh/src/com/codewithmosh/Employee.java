package com.codewithmosh;

public class Employee {
    private int baseSalary;
    private int extraHours;
    private int hourlyRate;

    public static int numberOfEmployees;


    public Employee(int baseSalary, int hourlyRate) {
        setBaseSalary(baseSalary);
        setHourlyRate(hourlyRate);
        numberOfEmployees++;
    }
    public Employee(int baseSalary) {
        this(baseSalary, 0);
    }

    public int calculateWage(int extraHours) {
        return baseSalary + extraHours * hourlyRate;
    }
    public int calculateWage() {
        return calculateWage(0);
    }


    private void setBaseSalary(int baseSalary) {
        if (baseSalary < 0)
            throw new IllegalArgumentException("Salary cannot be negative");
        this.baseSalary = baseSalary;
    }

    private void setExtraHours(int extraHours) {
        this.extraHours = extraHours;
    }

    private void setHourlyRate(int hourlyRate) {
        this.hourlyRate = hourlyRate;
    }
}