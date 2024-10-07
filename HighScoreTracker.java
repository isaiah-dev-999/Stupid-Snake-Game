import java.io.*;

public class HighScoreTracker {
    private static final String FILE_PATH = "high_score.txt";

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Please provide the score as an argument.");
            return;
        }

        int currentScore = Integer.parseInt(args[0]);
        int highScore = readHighScore();

        if (currentScore > highScore) {
            System.out.println("New high score: " + currentScore);
            writeHighScore(currentScore);
        } else {
            System.out.println("Current high score: " + highScore);
        }
    }

    private static int readHighScore() {
        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_PATH))) {
            return Integer.parseInt(reader.readLine());
        } catch (IOException | NumberFormatException e) {
            return 0; // Default high score if file doesn't exist or is invalid
        }
    }

    private static void writeHighScore(int newScore) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_PATH))) {
            writer.write(Integer.toString(newScore));
        } catch (IOException e) {
            System.out.println("Error writing high score.");
        }
    }
}
