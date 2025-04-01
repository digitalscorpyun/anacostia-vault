import pandas as pd  
import logging  

class BiasAudit:  
    def __init__(self, data_path: str, threshold: float = 0.15):  
        """  
        Initialize bias auditor with data and fairness threshold.  
        :param data_path: Path to CSV with 'salary' and 'demographic' columns.  
        :param threshold: Allowed disparity (e.g., 0.15 = 15%).  
        """  
        try:  
            self.data = pd.read_csv(data_path)  
            self.threshold = threshold  
            self._validate_columns()  
            logging.info("BiasAudit initialized successfully.")  
        except FileNotFoundError:  
            logging.error("Data file not found. Path: %s", data_path)  
            raise  

    def _validate_columns(self):  
        """Ensure required columns exist."""  
        required = {'salary', 'demographic'}  
        if not required.issubset(self.data.columns):  
            missing = required - set(self.data.columns)  
            raise ValueError(f"Missing columns: {missing}")  

    def flag_disparities(self) -> dict:  
        """Calculate median salary disparities across groups."""  
        results = {}  
        overall_median = self.data['salary'].median()  
        for group, group_data in self.data.groupby('demographic'):  
            group_median = group_data['salary'].median()  
            disparity = abs(group_median - overall_median) / overall_median  
            results[group] = {  
                'median_salary': group_median,  
                'disparity_ratio': disparity,  
                'exceeds_threshold': disparity > self.threshold  
            }  
        return results  

    def generate_report(self, output_path: str):  
        """Save disparities report as CSV."""  
        report = pd.DataFrame(self.flag_disparities()).T  
        report.to_csv(output_path, index_label='demographic_group')  
        logging.info("Report saved to: %s", output_path)  