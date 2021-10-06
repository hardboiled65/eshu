use std::error::Error;
use std::fmt;

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
            Locale::EnUs => "en",
            Locale::EnUk => "en",
            Locale::JaJp => "ja",
            Locale::KoKp => "ko",
            Locale::KoKr => "ko",
        }
    }
}
