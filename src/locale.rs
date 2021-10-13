use std::error::Error;
use std::fmt;

#[derive(Debug, PartialEq, Eq)]
#[repr(u16)]
pub enum Language {
    En,
    Ja,
    Ko,
}

impl fmt::Display for Language {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self)
    }
}

#[derive(Debug, PartialEq, Eq)]
#[repr(u16)]
pub enum Territory {
    Us,
    Uk,
    Jp,
    Kp,
    Kr,
}

impl fmt::Display for Territory {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self)
    }
}

#[derive(Debug, PartialEq, Eq)]
#[repr(u16)]
pub enum Locale {
    //----BEGIN LOCALE ENUM----
    EnUs,
    EnUk,
    JaJp,
    KoKp,
    KoKr,
    //----END LOCALE ENUM----
}

#[derive(Debug)]
pub struct NoLocaleError {
    locale: String,
}

impl Error for NoLocaleError {
    fn description(&self) -> &str {
        "No such locale."
    }
}

impl fmt::Display for NoLocaleError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "No such locale: {}", self.locale)
    }
}

impl Locale {
    pub fn new(string: &str) -> Result<Locale, NoLocaleError> {
        let string = string.replace("-", "_");
        match string.as_str() {
            //----BEGIN LOCALE NEW----
            "en_US" => Ok(Locale::EnUs),
            "en_UK" => Ok(Locale::EnUk),
            "ja_JP" => Ok(Locale::JaJp),
            "ko_KP" => Ok(Locale::KoKp),
            "ko_KR" => Ok(Locale::KoKr),
            //----END LOCALE NEW----
            _ => {
                Err(NoLocaleError {
                    locale: string.to_string(),
                })
            }
        }
    }

    pub fn language(&self) -> &str {
        match self {
            //----BEGIN LOCALE LANGUAGE----
            Locale::EnUs => "en",
            Locale::EnUk => "en",
            Locale::JaJp => "ja",
            Locale::KoKp => "ko",
            Locale::KoKr => "ko",
            //----END LOCALE LANGUAGE----
        }
    }

    pub fn territory(&self) -> &str {
        match self {
            //----BEGIN LOCALE TERRITORY----
            Locale::EnUs => "US",
            Locale::EnUk => "UK",
            Locale::JaJp => "JP",
            Locale::KoKp => "KP",
            Locale::KoKr => "KR",
            //----END LOCALE TERRITORY----
        }
    }
}
