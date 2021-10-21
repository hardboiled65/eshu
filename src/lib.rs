pub mod locale;

#[cfg(test)]
mod tests {
    use super::locale::{Language, Territory, Locale};

    #[test]
    fn language_to_string() {
        let lang = Language::Ko;
        assert_eq!(lang.to_string(), String::from("ko"));
    }

    #[test]
    fn territory_to_string() {
        let terr = Territory::Uk;
        assert_eq!(terr.to_string(), String::from("UK"));
    }

    #[test]
    fn compare_locales() {
        let locale = Locale::JaJp;
        assert_eq!(locale, Locale::JaJp);
    }

    #[test]
    fn locale_new() {
        // let locale1 = Locale::new("en_US");
        let locale2 = Locale::new("en-US");
        match locale2 {
            Ok(locale) => { println!("{:?}", locale); },
            Err(err) => {
                panic!("{}", err);
            },
        }
    }

    #[test]
    fn locale_language() {
        let locale = Locale::EnUk;
        assert_eq!(locale.language(), "en");
    }
}
