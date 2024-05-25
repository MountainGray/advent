mod manager;
mod tui;

use chrono;
use crossterm::event::{self, Event, KeyCode, KeyEvent, KeyEventKind};
use ratatui::{
    prelude::*,
    symbols::border,
    widgets::{block::*, *},
};
use std::io;

#[derive(Debug, Default)]
enum AdventState {
    #[default]
    MainMenu,
    YearMenu,
    DayMenu,
    Puzzle,
}

#[derive(Debug, Default)]
pub struct AdventTui {
    state: AdventState,
    exit: bool,
}

fn main() -> io::Result<()> {
    let mut terminal = tui::init()?;
    //println!("{}", manager::get_input(2017, 2));
    let app_result = AdventTui::default().run(&mut terminal);
    tui::restore()?;
    app_result
}

impl AdventTui {
    pub fn run(&mut self, terminal: &mut tui::Tui) -> io::Result<()> {
        while !self.exit {
            terminal.draw(|frame| self.render_frame(frame))?;
            self.handle_input()?;
        }
        Ok(())
    }

    fn render_frame(&self, frame: &mut Frame) {
        frame.render_widget(self, frame.size())
    }

    fn handle_input(&mut self) -> io::Result<()> {
        if event::poll(std::time::Duration::from_millis(10))? {
            match event::read()? {
                Event::Key(key_event) if key_event.kind == KeyEventKind::Press => {
                    self.handle_key_event(key_event)
                }
                _ => {}
            }
        }
        Ok(())
    }

    fn handle_key_event(&mut self, key_event: KeyEvent) {
        match key_event.code {
            KeyCode::Char('q') => self.exit = true,
            KeyCode::Left => match self.state {
                AdventState::MainMenu => {}
                AdventState::YearMenu => self.state = AdventState::MainMenu,
                AdventState::DayMenu => self.state = AdventState::YearMenu,
                AdventState::Puzzle => self.state = AdventState::DayMenu,
            },
            KeyCode::Right => match self.state {
                AdventState::MainMenu => self.state = AdventState::YearMenu,
                AdventState::YearMenu => self.state = AdventState::DayMenu,
                AdventState::DayMenu => self.state = AdventState::Puzzle,
                AdventState::Puzzle => {}
            },
            _ => {}
        }
    }
}

impl Widget for &AdventTui {
    fn render(self, area: Rect, buf: &mut Buffer) {
        let title = Title::from(
            match self.state {
                AdventState::MainMenu => "Main Menu",
                AdventState::YearMenu => "Year Menu",
                AdventState::DayMenu => "Day Menu",
                AdventState::Puzzle => "Puzzle",
            }
            .bold(),
        );

        let instrs = Title::from("TODO");
        let block = Block::default()
            .title(title)
            .title(
                instrs
                    .alignment(Alignment::Center)
                    .position(Position::Bottom),
            )
            .borders(Borders::ALL)
            .border_set(border::THICK)
            .style(Style::default().fg(Color::White).bg(Color::Black));

        let time = chrono::Local::now().format("%Y-%m-%d %h:%m:%s").to_string();

        Paragraph::new(time)
            .centered()
            .block(block)
            .style(Style::default().fg(Color::White).bg(Color::Black))
            .render(area, buf);
    }
}
