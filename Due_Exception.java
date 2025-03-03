package mio.pacchetto.prova;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    private static void ciao(int a) throws InputMismatchException {  // Generale: può lanciare qualsiasi eccezione
        Scanner tastiera = new Scanner(System.in);

        if(a<0)
            throw new IllegalArgumentException("ATTENTO ARGOMENTO NEGATIVO");

        int l = tastiera.nextInt();  // Se l'input non è un numero, genera InputMismatchException
        System.out.println("dopo");
    }

    public static void main(String[] args) {
        int l = -10;

        try {
            ciao(l);
        } catch (InputMismatchException e) {  // Cattura qualsiasi eccezione, inclusa InputMismatchException
            e.printStackTrace();
            System.out.println("Errore generico catturato: " + e.getMessage());
        }
        catch(IllegalArgumentException e)
        {
            e.printStackTrace();
            System.out.println("Argomnto negativo");
        }

    }
}