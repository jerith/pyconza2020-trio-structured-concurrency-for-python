;;; publish.el --- Publish reveal.js presentation from Org file
;; -*- Mode: Emacs-Lisp -*-
;; -*- coding: utf-8 -*-

;; SPDX-FileCopyrightText: 2017-2020 Jens Lechtenbörger
;; SPDX-License-Identifier: GPL-3.0-or-later

;; Modified by Jeremy Thurgood for the purposes of this project.

;;; License: GPL-3.0-or-later

;;; Commentary:
;; Publication of Org source files to reveal.js uses Org export
;; functionality offered by emacs-reveal, which bundles reveal.js with
;; several plugins and MELPA packages org-re-reveal,
;; org-re-reveal-ref, and oer-reveal.  Initialization code is provided
;; by emacs-reveal.
;;
;; Use this file from its parent directory with the following shell
;; command:
;; `emacs --batch --load elisp/publish.el'

;;; Code:
;; Setup dot.
;; The following supposes that png images are generated into directory img,
;; which needs to exist.
(make-directory "img" t)
(setq oer-reveal-publish-babel-languages '((dot . t) (emacs-lisp . t))
      org-publish-project-alist
      (list (list "img"
                  :base-directory "img"
                  :base-extension "png"
                  :publishing-function 'org-publish-attachment
                  :publishing-directory "./public/img")))

;; Use present environment.
(setq emacs-reveal-managed-install-p nil)

;; Load emacs-reveal.
(let ((install-dir
       (mapconcat #'file-name-as-directory
                  ;; Change this to poit to where emacs-reveal is installed.
                  `(,user-emacs-directory "third-party" "emacs-reveal") "")))
  (add-to-list 'load-path install-dir)
  (condition-case nil
      ;; Either require package with above hard-coded location
      ;; (e.g., in docker) ...
      (require 'emacs-reveal)
    (error
     ;; ... or look for sub-directory "emacs-reveal" of parent project.
     (add-to-list
      'load-path
      (expand-file-name "../../emacs-reveal/" (file-name-directory load-file-name)))
     (require 'emacs-reveal))))

;; ;; Add klipse plugin for live code execution.
;; (add-to-list 'oer-reveal-plugins "klipse-libs")

;; Stop complaining about this.
(setq python-indent-guess-indent-offset-verbose nil)
(setq-default indent-tabs-mode nil)

;; Publish Org files.
(oer-reveal-publish-all
 (list
  (list "images"
        :base-directory "./img"
        :base-extension (regexp-opt '("png"))
        :publishing-directory "./public/reveal.js/dist/img"
        :publishing-function 'org-publish-attachment)
  (list "theme-css"
        :base-directory "./css/theme"
        :base-extension 'any
        :publishing-directory "./public/reveal.js/dist/theme"
        :publishing-function 'org-publish-attachment)
  (list "other-css"
        :base-directory "./css"
        :base-extension 'any
        :publishing-directory "./public/reveal.js/dist"
        :publishing-function 'org-publish-attachment)))

;;; publish.el ends here
