use std::error::Error;
use std::fmt;

#[derive(Debug, PartialEq, Eq)]
#[repr(u16)]
pub enum Locale {
    EnUs,
    EnUk,
    JaJp,
    KoKr,
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
            "en_US" => Ok(Locale::EnUs),
            "en_UK" => Ok(Locale::EnUk),
            "ja_JP" => Ok(Locale::JaJp),
            "ko_KR" => Ok(Locale::KoKr),
            _ => {
                Err(NoLocaleError {
                    locale: string.to_string(),
                })
            }
        }
    }
}
