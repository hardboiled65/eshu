pub mod locale;

#[cfg(test)]
mod tests {
    use super::locale::{LanguageCode, TerritoryCode, Locale};

    #[test]
    fn language_code_to_string() {
        let lang = LanguageCode::Ko;
        assert_eq!(lang.to_string(), String::from("Ko"));
    }

    #[test]
    fn territory_code_to_string() {
        let terr = TerritoryCode::Uk;
        assert_eq!(terr.to_string(), String::from("Uk"));
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
