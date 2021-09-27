pub mod locale;

#[cfg(test)]
mod tests {
    use super::locale::Locale;

    #[test]
    fn compare_locales() {
        let locale = Locale::JaJp;
        assert_eq!(locale, Locale::JaJp);
    }

    #[test]
    fn locale_new() {
        // let locale1 = Locale::new("en_US");
        let locale2 = Locale::new("no_NO");
        match locale2 {
            Ok(locale) => { println!("{:?}", locale); },
            Err(err) => {
                panic!("{}", err);
            },
        }
    }
}