package VacuousWinners;


import java.awt.Component;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.util.ArrayList;

import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTextArea;
import VacuousWinners.GameLogic.*;

public class GameScreen extends Screen{
    private ChallengeControl gamecontrol;
    private Player p = new Player("Player1");

    public GameScreen(JFrame f) {
        super(f);
    }

    @Override
    public void draw() throws IOException {
        frame.getContentPane().setLayout(new GridLayout(0, 2));

        JSplitPane codeArea = new JSplitPane();
        codeArea.setOrientation(JSplitPane.VERTICAL_SPLIT);

        JPanel codeTop = new JPanel();
        JPanel codeBottom = new JPanel();
        codeTop.setMinimumSize(new Dimension(0, 200));
        codeBottom.setMinimumSize(new Dimension(0, 200));

        ArrayList<String> curr_challenge = gamecontrol.getNextChallenge();

        JTextArea codeInstructions = new JTextArea();
        codeInstructions.setEditable(false);
        codeInstructions.setText(curr_challenge.get(0));
        codeInstructions.setWrapStyleWord(true);
        codeInstructions.setLineWrap(true);
        codeInstructions.setFocusable(false);
        JScrollPane instructionsSroll = new JScrollPane(codeInstructions);

        JTextArea codeEditor = new JTextArea();
        codeEditor.setText(curr_challenge.get(1));
        JScrollPane codeScroll = new JScrollPane(codeEditor);

        codeTop.setLayout(new BoxLayout(codeTop, BoxLayout.Y_AXIS));
        codeBottom.setLayout(new BoxLayout(codeBottom, BoxLayout.Y_AXIS));

        JButton submitButton = new JButton("Submit");
        submitButton.setAlignmentX(Component.CENTER_ALIGNMENT);
        submitButton.setAlignmentX(Component.RIGHT_ALIGNMENT);

        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent evt) {
                gamecontrol.submitChallenge(codeEditor.getText(), p);
                submitButton.setText("Submitted");
                submitButton.setEnabled(false);
                // todo submit code
                System.out.println(codeEditor.getText());
            }
        });

        codeTop.add(instructionsSroll);
        codeBottom.add(codeScroll);
        codeBottom.add(Box.createRigidArea(new Dimension(0,10)));
        codeBottom.add(submitButton);
        codeBottom.add(Box.createRigidArea(new Dimension(0,10)));

        codeArea.setTopComponent(codeTop);
        codeArea.setBottomComponent(codeBottom);

        frame.add(codeArea);

        frame.repaint();
        frame.revalidate();
    }
}
