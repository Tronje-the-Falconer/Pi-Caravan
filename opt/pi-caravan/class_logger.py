class Logger():
    def __init__(self, filename):
        self.filename = filename
    def create_logger(self):
        """
        creating loggers
        """
        check_website_logfile()
        loglevel_file_value = database_get_logging_value.get_logging_value(names.loglevel_file_field)
        loglevel_console_value = database_get_logging_value.get_logging_value(names.loglevel_console_field)
        
        # Logger fuer website
        website_log_rotatingfilehandler = logging.handlers.RotatingFileHandler(paths.get_path_logfile_txt_file(), mode='a', maxBytes=1048576, backupCount=36, encoding=None, delay=False)
        website_log_rotatingfilehandler.setLevel(logging.INFO)
        website_log_rotatingfilehandler_formatter = logging.Formatter('%(asctime)s %(message)s', '%y-%m-%d %H:%M:%S')
        website_log_rotatingfilehandler.setFormatter(website_log_rotatingfilehandler_formatter)

        # Logger fuer pi-caravan debugging
        pi_caravan_log_rotatingfilehandler = logging.handlers.RotatingFileHandler(paths.get_pi_caravan_log_file_path(), mode='a', maxBytes=2097152, backupCount=20, encoding=None, delay=False)
        pi_caravan_log_rotatingfilehandler.setLevel(get_logginglevel(loglevel_file_value))
        pi_caravan_log_rotatingfilehandler_formatter = logging.Formatter('%(asctime)s %(name)-27s %(levelname)-8s %(message)s', '%m-%d %H:%M:%S')
        pi_caravan_log_rotatingfilehandler.setFormatter(pi_caravan_log_rotatingfilehandler_formatter)

        # Logger fuer die Console
        console_streamhandler = logging.StreamHandler()
        console_streamhandler.setLevel(get_logginglevel(loglevel_console_value))
        console_streamhandler_formatter = logging.Formatter(' %(levelname)-10s: %(name)-8s %(message)s')
        console_streamhandler.setFormatter(console_streamhandler_formatter)
        
        logger = logging.getLogger(pythonfile)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(website_log_rotatingfilehandler)
        logger.addHandler(pi_caravan_log_rotatingfilehandler)
        logger.addHandler(console_streamhandler)
        
        return logger