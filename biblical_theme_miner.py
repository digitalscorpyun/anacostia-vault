<<<<<<< HEAD
"""
biblical_theme_miner.py (v3.4)
4GB-RAM Optimized Edition
"""

import os
import re
import gc
import time
import nltk
import traceback
import PyPDF2
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# ========== OCR CONFIGURATION ==========
POPPLER_PATH = r"C:\poppler\Library\bin"
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

try:
    from pdf2image import convert_from_path
    import pytesseract
    import psutil
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
except ImportError as e:
    print(f"Missing package: {str(e)}")

# ========== NLTK INITIALIZATION ==========
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

class NASBAnalyzer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.setup_directories()
        
        # Optimized regex pattern
        self.nasb_pattern = re.compile(
            r'(\d{1,3}\s?[A-Za-z]+\s\d+:\d+)\s+(.*?)(?=\d{1,3}\s?[A-Za-z]+\s\d+:\d+|$)',
            re.DOTALL | re.IGNORECASE
        )

    def setup_directories(self):
        """Ensure directory structure"""
        Path("data/cones_works").mkdir(parents=True, exist_ok=True)
        Path("output").mkdir(exist_ok=True)
        self.log("Directory structure validated", "SUCCESS")

    def log(self, message, level="INFO"):
        """Enhanced logging with memory tracking"""
        colors = {
            "DEBUG": "\033[36m", "INFO": "\033[94m",
            "SUCCESS": "\033[92m", "WARNING": "\033[93m",
            "ERROR": "\033[91m"
        }
        mem_usage = self.memory_usage()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"{colors.get(level, '')}[{timestamp} {level}] [{mem_usage}% MEM] {message}\033[0m"
        print(log_msg)

    def memory_usage(self):
        """Get current memory usage percentage"""
        try:
            return psutil.virtual_memory().percent
        except:
            return "??"

    def load_nasb_bible(self):
        """Memory-aware Bible loader"""
        nasb_path = Path("data/cones_works/holy-bible-nasb.pdf")
        bible = {}
        
        try:
            bible = self._load_pdf_text(nasb_path)
            if not bible:
                self.log("Initiating 4GB-optimized OCR...", "WARNING")
                bible = self._load_pdf_ocr(nasb_path)
            return bible
        except Exception as e:
            self.log(f"Bible load failed: {str(e)}", "ERROR")
            return {}

    def _load_pdf_text(self, pdf_path):
        """Standard PDF text extraction"""
        bible = {}
        try:
            with open(pdf_path, 'rb') as f:
                pdf = PyPDF2.PdfReader(f)
                if len(pdf.pages) == 0:
                    self.log("Empty PDF detected", "ERROR")
                    return bible

                # Sample page diagnostic
                test_page = min(100, len(pdf.pages)-1)
                test_text = pdf.pages[test_page].extract_text() or ''
                self.log(f"Page {test_page} sample: {test_text[:200]}", "DEBUG")

                for page in pdf.pages:
                    text = page.extract_text() or ''
                    for ref, content in self.nasb_pattern.findall(text):
                        clean_ref = ref.strip()
                        bible[clean_ref] = ' '.join(content.split())
            
            self.log(f"Loaded {len(bible)} verses via PDF", "SUCCESS")
            return bible
            
        except PyPDF2.errors.PdfReadError as e:
            self.log(f"PDF read error: {str(e)}", "ERROR")
            return {}

    def _load_pdf_ocr(self, pdf_path):
        """4GB-RAM Optimized OCR Processing"""
        bible = {}
        try:
            # Windows-specific memory constraints
            if os.name == 'nt':
                try:
                    try:
                        try:
                            from win32api import SetProcessWorkingSetSize
                        except ImportError:
                            self.log("win32api not installed - using default memory", "WARNING")
                    except ImportError:
                        self.log("win32api not installed - using default memory", "WARNING")
                    SetProcessWorkingSetSize(-1, 1<<28, 1<<30)  # 256MB-1GB
                except ImportError:
                    self.log("pywin32 not installed - using default memory", "WARNING")

            # Memory-sensitive processing parameters
            chunk_size = 10  # Pages per chunk
            dpi_setting = 150
            jpeg_quality = 85

            total_pages = len(convert_from_path(
                str(pdf_path), 
                poppler_path=POPPLER_PATH, 
                dpi=dpi_setting, 
                thread_count=1
            ))
            
            for start_page in range(0, total_pages, chunk_size):
                end_page = min(start_page + chunk_size, total_pages)
                self.log(f"Processing pages {start_page+1}-{end_page}...", "INFO")
                
                # Load current chunk with optimized settings
                images = convert_from_path(
                    str(pdf_path),
                    poppler_path=POPPLER_PATH,
                    dpi=dpi_setting,
                    thread_count=1,
                    grayscale=True,
                    fmt='jpeg',
                    jpegopt={"quality": jpeg_quality},
                    first_page=start_page+1,
                    last_page=end_page
                )
                
                for page_num, img in enumerate(images, start=start_page):
                    try:
                        # Memory-optimized OCR
                        text = pytesseract.image_to_string(
                            img, 
                            timeout=90,
                            config='--psm 6 -c preserve_interword_spaces=1'
                        )
                        for ref, content in self.nasb_pattern.findall(text):
                            clean_ref = ref.strip()
                            bible[clean_ref] = ' '.join(content.split())
                        
                        # Aggressive resource cleanup
                        img.fp = None  # Break PIL reference cycle
                        del img
                        gc.collect()
                        
                    except Exception as e:
                        self.log(f"Skipped page {page_num+1}: {str(e)}", "WARNING")
                
                # Chunk cleanup
                del images
                gc.collect()
                
                # Emergency memory management
                try:
                    if psutil.virtual_memory().percent > 85:
                        self.log("Memory threshold exceeded - emergency cleanup", "WARNING")
                        gc.collect()
                        time.sleep(5)  # Allow GC to complete
                except NameError:
                    pass  # psutil not available

            self.log(f"OCR extracted {len(bible)} verses", "SUCCESS")
            return bible
            
        except Exception as e:
            self.log(f"OCR failure: {str(e)}", "ERROR")
            return {}

    def load_cones_works(self):
        """Process James Cone's PDF works with memory checks"""
        cone_texts = {}
        cone_dir = Path("data/cones_works")
        
        for pdf_file in cone_dir.glob("*.pdf"):
            if "holy-bible" in pdf_file.name.lower():
                continue

            try:
                with open(pdf_file, 'rb') as f:
                    pdf = PyPDF2.PdfReader(f)
                    text = ' '.join([
                        page.extract_text() or '' 
                        for page in pdf.pages 
                    ])
                    cone_texts[pdf_file.name] = text
                    self.log(f"Processed {pdf_file.name} ({len(text):,} chars)", "SUCCESS")
                    gc.collect()  # Cleanup after each file
            except Exception as e:
                self.log(f"Failed {pdf_file.name}: {str(e)}", "ERROR")
        
        return cone_texts

    def analyze_theme(self, theme="deliverance"):
        """Memory-aware analysis workflow"""
        # Load data sources
        bible = self.load_nasb_bible()
        cone_texts = self.load_cones_works()
        
        if not bible or not cone_texts:
            self.log("Analysis aborted: Missing essential data", "ERROR")
            return

        # Prepare analysis corpus
        corpus = list(bible.values()) + list(cone_texts.values())
        doc_names = list(bible.keys()) + list(cone_texts.keys())

        # TF-IDF processing with memory efficiency
        tfidf = TfidfVectorizer(
            preprocessor=self.preprocess_text,
            stop_words=list(self.stop_words),
            max_features=10000  # Limit vocabulary size
        )
        matrix = tfidf.fit_transform(corpus)
        theme_vec = tfidf.transform([theme])
        
        # Generate connections
        connections = []
        scores = matrix.dot(theme_vec.T).toarray().flatten()
        for idx, score in enumerate(scores):
            if score > 0.15:
                connections.append((doc_names[idx], score))
        
        if connections:
            self._visualize_network(connections, theme)
        else:
            self.log("No significant connections found", "WARNING")

    def preprocess_text(self, text):
        """Text normalization pipeline"""
        tokens = word_tokenize(text.lower())
        filtered = [
            self.lemmatizer.lemmatize(word)
            for word in tokens
            if word.isalnum() and word not in self.stop_words
        ]
        return ' '.join(filtered)

    def _visualize_network(self, connections, theme):
        """Generate optimized network visualization"""
        G = nx.Graph()
        for node, weight in connections:
            G.add_node(node, weight=weight)
        
        # Create edges between similar nodes
        nodes = list(G.nodes(data=True))
        for i, (n1, d1) in enumerate(nodes):
            for n2, d2 in nodes[i+1:]:
                if abs(d1['weight'] - d2['weight']) < 0.1:
                    G.add_edge(n1, n2)
        
        # Generate visualization
        plt.figure(figsize=(20, 20))
        pos = nx.spring_layout(G, k=0.5)  # Reduced repulsion
        nx.draw(G, pos, with_labels=True, 
               node_size=600, font_size=8, alpha=0.8)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"output/{theme}_network_{timestamp}.png"
        plt.savefig(output_file, bbox_inches='tight', dpi=100)  # Reduced resolution
        plt.close()  # Prevent figure accumulation
        self.log(f"Network visualization saved to {output_file}", "SUCCESS")

if __name__ == "__main__":
    analyzer = NASBAnalyzer()
=======
"""
biblical_theme_miner.py (v3.4)
4GB-RAM Optimized Edition
"""

import os
import re
import gc
import time
import nltk
import traceback
import PyPDF2
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# ========== OCR CONFIGURATION ==========
POPPLER_PATH = r"C:\poppler\Library\bin"
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

try:
    from pdf2image import convert_from_path
    import pytesseract
    import psutil
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
except ImportError as e:
    print(f"Missing package: {str(e)}")

# ========== NLTK INITIALIZATION ==========
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

class NASBAnalyzer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.setup_directories()
        
        # Optimized regex pattern
        self.nasb_pattern = re.compile(
            r'(\d{1,3}\s?[A-Za-z]+\s\d+:\d+)\s+(.*?)(?=\d{1,3}\s?[A-Za-z]+\s\d+:\d+|$)',
            re.DOTALL | re.IGNORECASE
        )

    def setup_directories(self):
        """Ensure directory structure"""
        Path("data/cones_works").mkdir(parents=True, exist_ok=True)
        Path("output").mkdir(exist_ok=True)
        self.log("Directory structure validated", "SUCCESS")

    def log(self, message, level="INFO"):
        """Enhanced logging with memory tracking"""
        colors = {
            "DEBUG": "\033[36m", "INFO": "\033[94m",
            "SUCCESS": "\033[92m", "WARNING": "\033[93m",
            "ERROR": "\033[91m"
        }
        mem_usage = self.memory_usage()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"{colors.get(level, '')}[{timestamp} {level}] [{mem_usage}% MEM] {message}\033[0m"
        print(log_msg)

    def memory_usage(self):
        """Get current memory usage percentage"""
        try:
            return psutil.virtual_memory().percent
        except:
            return "??"

    def load_nasb_bible(self):
        """Memory-aware Bible loader"""
        nasb_path = Path("data/cones_works/holy-bible-nasb.pdf")
        bible = {}
        
        try:
            bible = self._load_pdf_text(nasb_path)
            if not bible:
                self.log("Initiating 4GB-optimized OCR...", "WARNING")
                bible = self._load_pdf_ocr(nasb_path)
            return bible
        except Exception as e:
            self.log(f"Bible load failed: {str(e)}", "ERROR")
            return {}

    def _load_pdf_text(self, pdf_path):
        """Standard PDF text extraction"""
        bible = {}
        try:
            with open(pdf_path, 'rb') as f:
                pdf = PyPDF2.PdfReader(f)
                if len(pdf.pages) == 0:
                    self.log("Empty PDF detected", "ERROR")
                    return bible

                # Sample page diagnostic
                test_page = min(100, len(pdf.pages)-1)
                test_text = pdf.pages[test_page].extract_text() or ''
                self.log(f"Page {test_page} sample: {test_text[:200]}", "DEBUG")

                for page in pdf.pages:
                    text = page.extract_text() or ''
                    for ref, content in self.nasb_pattern.findall(text):
                        clean_ref = ref.strip()
                        bible[clean_ref] = ' '.join(content.split())
            
            self.log(f"Loaded {len(bible)} verses via PDF", "SUCCESS")
            return bible
            
        except PyPDF2.errors.PdfReadError as e:
            self.log(f"PDF read error: {str(e)}", "ERROR")
            return {}

    def _load_pdf_ocr(self, pdf_path):
        """4GB-RAM Optimized OCR Processing"""
        bible = {}
        try:
            # Windows-specific memory constraints
            if os.name == 'nt':
                try:
                    try:
                        try:
                            from win32api import SetProcessWorkingSetSize
                        except ImportError:
                            self.log("win32api not installed - using default memory", "WARNING")
                    except ImportError:
                        self.log("win32api not installed - using default memory", "WARNING")
                    SetProcessWorkingSetSize(-1, 1<<28, 1<<30)  # 256MB-1GB
                except ImportError:
                    self.log("pywin32 not installed - using default memory", "WARNING")

            # Memory-sensitive processing parameters
            chunk_size = 10  # Pages per chunk
            dpi_setting = 150
            jpeg_quality = 85

            total_pages = len(convert_from_path(
                str(pdf_path), 
                poppler_path=POPPLER_PATH, 
                dpi=dpi_setting, 
                thread_count=1
            ))
            
            for start_page in range(0, total_pages, chunk_size):
                end_page = min(start_page + chunk_size, total_pages)
                self.log(f"Processing pages {start_page+1}-{end_page}...", "INFO")
                
                # Load current chunk with optimized settings
                images = convert_from_path(
                    str(pdf_path),
                    poppler_path=POPPLER_PATH,
                    dpi=dpi_setting,
                    thread_count=1,
                    grayscale=True,
                    fmt='jpeg',
                    jpegopt={"quality": jpeg_quality},
                    first_page=start_page+1,
                    last_page=end_page
                )
                
                for page_num, img in enumerate(images, start=start_page):
                    try:
                        # Memory-optimized OCR
                        text = pytesseract.image_to_string(
                            img, 
                            timeout=90,
                            config='--psm 6 -c preserve_interword_spaces=1'
                        )
                        for ref, content in self.nasb_pattern.findall(text):
                            clean_ref = ref.strip()
                            bible[clean_ref] = ' '.join(content.split())
                        
                        # Aggressive resource cleanup
                        img.fp = None  # Break PIL reference cycle
                        del img
                        gc.collect()
                        
                    except Exception as e:
                        self.log(f"Skipped page {page_num+1}: {str(e)}", "WARNING")
                
                # Chunk cleanup
                del images
                gc.collect()
                
                # Emergency memory management
                try:
                    if psutil.virtual_memory().percent > 85:
                        self.log("Memory threshold exceeded - emergency cleanup", "WARNING")
                        gc.collect()
                        time.sleep(5)  # Allow GC to complete
                except NameError:
                    pass  # psutil not available

            self.log(f"OCR extracted {len(bible)} verses", "SUCCESS")
            return bible
            
        except Exception as e:
            self.log(f"OCR failure: {str(e)}", "ERROR")
            return {}

    def load_cones_works(self):
        """Process James Cone's PDF works with memory checks"""
        cone_texts = {}
        cone_dir = Path("data/cones_works")
        
        for pdf_file in cone_dir.glob("*.pdf"):
            if "holy-bible" in pdf_file.name.lower():
                continue

            try:
                with open(pdf_file, 'rb') as f:
                    pdf = PyPDF2.PdfReader(f)
                    text = ' '.join([
                        page.extract_text() or '' 
                        for page in pdf.pages 
                    ])
                    cone_texts[pdf_file.name] = text
                    self.log(f"Processed {pdf_file.name} ({len(text):,} chars)", "SUCCESS")
                    gc.collect()  # Cleanup after each file
            except Exception as e:
                self.log(f"Failed {pdf_file.name}: {str(e)}", "ERROR")
        
        return cone_texts

    def analyze_theme(self, theme="deliverance"):
        """Memory-aware analysis workflow"""
        # Load data sources
        bible = self.load_nasb_bible()
        cone_texts = self.load_cones_works()
        
        if not bible or not cone_texts:
            self.log("Analysis aborted: Missing essential data", "ERROR")
            return

        # Prepare analysis corpus
        corpus = list(bible.values()) + list(cone_texts.values())
        doc_names = list(bible.keys()) + list(cone_texts.keys())

        # TF-IDF processing with memory efficiency
        tfidf = TfidfVectorizer(
            preprocessor=self.preprocess_text,
            stop_words=list(self.stop_words),
            max_features=10000  # Limit vocabulary size
        )
        matrix = tfidf.fit_transform(corpus)
        theme_vec = tfidf.transform([theme])
        
        # Generate connections
        connections = []
        scores = matrix.dot(theme_vec.T).toarray().flatten()
        for idx, score in enumerate(scores):
            if score > 0.15:
                connections.append((doc_names[idx], score))
        
        if connections:
            self._visualize_network(connections, theme)
        else:
            self.log("No significant connections found", "WARNING")

    def preprocess_text(self, text):
        """Text normalization pipeline"""
        tokens = word_tokenize(text.lower())
        filtered = [
            self.lemmatizer.lemmatize(word)
            for word in tokens
            if word.isalnum() and word not in self.stop_words
        ]
        return ' '.join(filtered)

    def _visualize_network(self, connections, theme):
        """Generate optimized network visualization"""
        G = nx.Graph()
        for node, weight in connections:
            G.add_node(node, weight=weight)
        
        # Create edges between similar nodes
        nodes = list(G.nodes(data=True))
        for i, (n1, d1) in enumerate(nodes):
            for n2, d2 in nodes[i+1:]:
                if abs(d1['weight'] - d2['weight']) < 0.1:
                    G.add_edge(n1, n2)
        
        # Generate visualization
        plt.figure(figsize=(20, 20))
        pos = nx.spring_layout(G, k=0.5)  # Reduced repulsion
        nx.draw(G, pos, with_labels=True, 
               node_size=600, font_size=8, alpha=0.8)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"output/{theme}_network_{timestamp}.png"
        plt.savefig(output_file, bbox_inches='tight', dpi=100)  # Reduced resolution
        plt.close()  # Prevent figure accumulation
        self.log(f"Network visualization saved to {output_file}", "SUCCESS")

if __name__ == "__main__":
    analyzer = NASBAnalyzer()
>>>>>>> 769b11b2f1b8510b1da5db510583301e7c9784a9
    analyzer.analyze_theme(theme="deliverance")